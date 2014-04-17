
In the repo you want to summarize:

```
git log --author=im@danmarvelo.us --no-merges \
    --author=danofames@gmail.com --author="Dan Conner" --author=danofames@gmail.com \
    --numstat --date=iso --format=format:"%h%x09%ad" \
    | python $SBINDIR/formatgitstatsforsummary -i bootstrap-tab\.js -i \/migrations\/

```