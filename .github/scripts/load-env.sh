awk '!/^#/{print}' < build.env >> "$GITHUB_ENV"
