#!/bin/bash
# Runs whatq over CC-100.

set -eou pipefail

readonly LGCODES=(
    af am ar as az be bg bn bn_rom br bs ca cs cy da de el en eo es et eu fa
    ff fi fr fy ga gd gl gn gu ha he hi hi_rom hr ht hu hy id ig is it ja jv
    ka kk km kn no ku ky la lg li ln lo lt lv mg mk ml mn mr ms my my_zaw ne
    nl no ns om or pa pl ps pt qu rm ro ru sa si sc sd sk sl so sq sr ss su
    sv sw ta ta_rom te te_rom th tl tn tr ug uk ur ur_rom uz vi wo xh yi yo
    zh_Hans zh-Hant zu)

main() {
   for LGCODE in "${LGCODES[@]}"; do
       LOCAL="${LGCODE}.txt.xz"
       curl -s -O "https://data.statmt.org/cc-100/${LOCAL}"
       printf "%s\t" "${LGCODE}"
       ./whatq.py --xz "${LOCAL}"
       rm ${LOCAL}
       echo
   done
}

main
