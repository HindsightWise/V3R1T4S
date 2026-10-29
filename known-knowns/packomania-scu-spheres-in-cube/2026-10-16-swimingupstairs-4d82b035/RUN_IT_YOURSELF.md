# Run it yourself (from this folder, fresh shell)
sh verify-it-yourself/run_checks.sh
# expected output: see verify-it-yourself/RECEIPTS.md, last line PASS
# Not-isometric check: download https://packomania.com/scu/txt/scu_coords.tar.gz, extract scu884.txt and scu881.txt; the posted files differ (different centre sets / counts; on 2026-10-16 the posted scu881.txt listed 880 centres with a blank 881st row; it now lists all 881: see the maintainer note of 2026-10-28 in README.md).
# Rebuild: see how-we-built-it/README.md (start from Lu Peng's posted scu880.txt).
