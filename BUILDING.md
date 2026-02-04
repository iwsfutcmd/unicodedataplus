# Updating

## Bumping Unicode version

Instructions for *only* bumping the Unicode version:

1. In `makeunicodedata.py`:
    1. Modify `UNIDATA_VERSION` to applicable version.
    2. Update `cjk_ranges` to match new Unicode version data.
2. In `unicodedata.c`:
    1. Update `is_unified_ideograph()` to match new Unicode version data.
3. Run `makeunicodedata.py`.
4. Add some test cases to `test_unicodedataplus.py`.

## Rebuilding `unicodedata.c.h`

`unicodedata.c.h` (and `unicodedata.3.12.c.h`) are built using `cpython`'s Argument Clinic. 

To generate them, make sure the `cpython` repo is cloned somewhere, and run `./generate_headers.sh path_to_cpython_repo`

