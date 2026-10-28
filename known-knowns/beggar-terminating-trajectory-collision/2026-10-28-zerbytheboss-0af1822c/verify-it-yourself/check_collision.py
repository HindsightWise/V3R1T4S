#!/usr/bin/env python3
"""Standalone verifier for beggar-terminating-trajectory-collision.
Reads object/collision_witness.json, executes the deterministic BMN trick transition map,
and rigorously verifies:
1. Valid legal setting (N, R) = (16, 2)
2. Card counts and multiset conservation ({0: 8, 1: 4, 2: 4})
3. Distinct balanced initial deals s1 != s2
4. Reachable distinct playable trick-boundary states x != y
5. Exact trick collision F(x) == F(y) == z
6. Continuation from z terminates legally in 3 tricks with Player A winning all 16 cards
7. No infinite loops or shared pre-collision orbits
"""

import json
import sys
import os
from typing import List, Tuple, Optional, Dict
from dataclasses import dataclass

@dataclass(frozen=True)
class TrickState:
    deck_a: Tuple[int, ...]
    deck_b: Tuple[int, ...]
    leader: str

    def is_playable(self) -> bool:
        return len(self.deck_a) > 0 and len(self.deck_b) > 0

    def serialize(self) -> str:
        da = ','.join(map(str, self.deck_a))
        db = ','.join(map(str, self.deck_b))
        return f"(dA=[{da}], dB=[{db}], leader={self.leader})"

@dataclass
class TrickResult:
    next_state: TrickState
    is_terminal: bool
    winner: str
    moves: List[Tuple[str, int]]
    pile: List[int]

def opponent(player: str) -> str:
    return 'B' if player == 'A' else 'A'

def play_trick(state: TrickState) -> TrickResult:
    da = list(state.deck_a)
    db = list(state.deck_b)
    pile: List[int] = []
    moves: List[Tuple[str, int]] = []

    current_player = state.leader
    challenger: Optional[str] = None
    cards_to_play: int = 1

    while True:
        deck = da if current_player == 'A' else db

        if len(deck) == 0:
            winner = opponent(current_player)
            winner_deck = da if winner == 'A' else db
            winner_deck.extend(pile)
            return TrickResult(
                next_state=TrickState(tuple(da), tuple(db), winner),
                is_terminal=True,
                winner=winner,
                moves=moves,
                pile=pile,
            )

        card = deck.pop(0)
        pile.append(card)
        moves.append((current_player, card))

        if card > 0:
            challenger = current_player
            cards_to_play = card
            current_player = opponent(current_player)
        else:
            if challenger is not None:
                cards_to_play -= 1
                if cards_to_play == 0:
                    winner = challenger
                    winner_deck = da if winner == 'A' else db
                    winner_deck.extend(pile)
                    return TrickResult(
                        next_state=TrickState(tuple(da), tuple(db), winner),
                        is_terminal=False,
                        winner=winner,
                        moves=moves,
                        pile=pile,
                    )
            else:
                current_player = opponent(current_player)

def main():
    try:
        obj_path = os.path.join(os.path.dirname(__file__), "..", "object", "collision_witness.json")
        if not os.path.isfile(obj_path):
            obj_path = "object/collision_witness.json"
        
        with open(obj_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data.get("target_id") == "beggar-terminating-trajectory-collision", "Incorrect target_id"
        setting = data["deck_setting"]
        assert setting["N"] == 16 and setting["special_ranks"] == 2 and setting["cards_per_player"] == 8

        deals = data["initial_deals"]
        d1 = deals["deal1"]
        d2 = deals["deal2"]

        d1_a, d1_b = tuple(d1["deck_a"]), tuple(d1["deck_b"])
        d2_a, d2_b = tuple(d2["deck_a"]), tuple(d2["deck_b"])

        # 1. Deck size and balanced check
        assert len(d1_a) == 8 and len(d1_b) == 8, "Deal 1 must have 8 cards per player"
        assert len(d2_a) == 8 and len(d2_b) == 8, "Deal 2 must have 8 cards per player"
        assert d1["leader"] == "A" and d2["leader"] == "A", "Initial leader must be Player A"

        # 2. Multiset conservation: exactly eight 0s, four 1s, four 2s
        def multiset(da, db):
            counts = {0: 0, 1: 0, 2: 0}
            for c in da + db:
                assert c in counts, f"Invalid card value {c}"
                counts[c] += 1
            return counts

        assert multiset(d1_a, d1_b) == {0: 8, 1: 4, 2: 4}, "Deal 1 multiset mismatch"
        assert multiset(d2_a, d2_b) == {0: 8, 1: 4, 2: 4}, "Deal 2 multiset mismatch"

        # 3. Deals must be distinct
        assert (d1_a, d1_b) != (d2_a, d2_b), "Deals 1 and 2 must be distinct"

        s1_0 = TrickState(d1_a, d1_b, "A")
        s2_0 = TrickState(d2_a, d2_b, "A")

        # 4. Trajectory 1 Trick 1 -> state x
        r1_1 = play_trick(s1_0)
        state_x = r1_1.next_state
        expected_x = TrickState(tuple(data["predecessors"]["state_x"]["deck_a"]),
                                tuple(data["predecessors"]["state_x"]["deck_b"]),
                                data["predecessors"]["state_x"]["leader"])
        assert state_x == expected_x, f"State x mismatch: {state_x} vs {expected_x}"

        # 5. Trajectory 2 Trick 1 -> state y
        r2_1 = play_trick(s2_0)
        state_y = r2_1.next_state
        expected_y = TrickState(tuple(data["predecessors"]["state_y"]["deck_a"]),
                                tuple(data["predecessors"]["state_y"]["deck_b"]),
                                data["predecessors"]["state_y"]["leader"])
        assert state_y == expected_y, f"State y mismatch: {state_y} vs {expected_y}"

        # 6. Distinct playable predecessors
        assert state_x != state_y, "States x and y must be distinct"
        assert state_x.is_playable() and state_y.is_playable(), "States x and y must be playable"

        # 7. Collision step: F(x) == F(y) == z
        rx = play_trick(state_x)
        ry = play_trick(state_y)
        z_x = rx.next_state
        z_y = ry.next_state
        assert z_x == z_y, f"Collision failed: F(x)={z_x} != F(y)={z_y}"

        expected_z = TrickState(tuple(data["collision_state_z"]["deck_a"]),
                                tuple(data["collision_state_z"]["deck_b"]),
                                data["collision_state_z"]["leader"])
        assert z_x == expected_z, f"Collision state mismatch: {z_x} vs {expected_z}"

        # 8. Suffix continuation to termination
        curr = z_x
        suffix_tricks = 0
        visited = {curr: 0}
        terminated = False

        while suffix_tricks < 50:
            res = play_trick(curr)
            suffix_tricks += 1
            if res.is_terminal:
                terminated = True
                assert res.winner == "A", "Winner must be Player A"
                assert len(res.next_state.deck_a) == 16, "Player A must accumulate all 16 cards"
                assert len(res.next_state.deck_b) == 0, "Player B must have 0 cards"
                break
            assert res.next_state not in visited, f"Suffix entered a loop at trick {suffix_tricks}"
            visited[res.next_state] = suffix_tricks
            curr = res.next_state

        assert terminated, "Suffix did not terminate"
        assert suffix_tricks == 3, f"Expected 3 suffix tricks to termination, got {suffix_tricks}"
        assert data["continuation_to_termination"]["tricks_to_termination"] == 3

        # 9. Verify separate orbits prior to collision
        assert s1_0 != state_y and s2_0 != state_x, "Initial deals must not be on each other's trajectories"

        print("All Beggar-My-Neighbour collision conditions verified successfully!")
        print("PASS")
        sys.exit(0)

    except Exception as e:
        print(f"VERIFICATION FAILURE: {e}")
        print("FAIL")
        sys.exit(1)

if __name__ == "__main__":
    main()
