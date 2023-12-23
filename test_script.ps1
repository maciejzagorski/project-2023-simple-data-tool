$users = @("ella.b74@example.org", "876543216")
$passwords = @("+vJCXfFLe0", "Q3XWW+Uc*Z")
$actions = @("print-all-accounts", "print-oldest-account", "group-by-age", "print-children",
             "find-similar-children-by-age")

For ($i=0; $i -lt $users.Length; $i++) {
    For ($j=0; $j -lt $actions.Length; $j++) {
        python script.py --login $users[$i] --password $passwords[$i] $actions[$j]
        python script.py --login $users[$i] --password $passwords[$i] $actions[$j] create-database
        }
    }

