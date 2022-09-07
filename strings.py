DEFAULT_LANG_EXT = "cpp"
CURR_CONFIG_PROMPT = "Your current configuration is: "
CODE_TEMPLATE = "cpp_template.txt"
SUCCESS_MSG = "created the directly successfully"
TEST_SUCCESS = "Test success in creating folder, cleaning up"
CLEANUP_SUCCESS = "Cleanup done, tests complete"
TEST_FOLDER_NAME = "test_contest"

HELP_STRINGS = {
    "NAME_HELP": "The name of the directory, preferably the name of the contest.",
    "COUNT_HELP": "The number of files to be created, defaults to 6.",
    "LANG_HELP": "The programming language used, same for all files, defaults to C++. Only the extension needs to provided.",
    "TARGET_HELP": "The directory where the create the folder, defaults to pwd.",
    "VERBOSE_HELP": "This will make cphelper print messages to the console"
}

CPP_TEMPLATE = "/*\n        __                           ______   ________\n_____  |  | _______    ____   ____  /  __  \\ /  _____/\n\\__  \\ |  |/ /\\__  \\  /    \\_/ __ \\ >      </   __  \\\n / __ \\|    <  / __ \\|   |  \\  ___//   --   \\  |__\\  \\\n(____  /__|_ \\(____  /___|  /\\___  >______  /\\_____  /\n     \\/     \\/     \\/     \\/     \\/       \\/       \\/\n\n\n */\n\n#include <bits/stdc++.h>\n#define ll long long\n#define MAX 1000003\n#define pii pair<int,int>\n#define VP vector< pii >\n#define MOD 1000000007\n#define mp make_pair\n#define pb push_back\n#define rep(i,a,b) for(int (i) = (a); (i) < (b); (i)++)\n#define all(v) (v).begin(),(v).end()\n#define S(x) scanf(\"%d\",&(x))\n#define S2(x,y) scanf(\"%d%d\",&(x),&(y))\n#define SL(x) scanf(\"%lld\",&(x))\n#define SL2(x) scanf(\"%lld%lld\",&(x),&(y))\n#define P(x) printf(\"%d\\n\",(x))\n#define FF first\n#define SS second\n\nusing namespace std;\nint main() {\n#ifndef ONLINE_JUDGE\n\tfreopen(\"input1.txt\", \"r\", stdin);\n\tfreopen(\"output1.txt\", \"w\", stdout);\n#endif\n\n\tll n, t;\n\tcin >> t;\n\twhile (t--) {\n\t\tcin >> n;\n\t}\n\n}"
