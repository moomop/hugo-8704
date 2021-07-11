# hugo-8704
Reproducer for https://github.com/gohugoio/hugo/issues/8704

Test which runs hugo 100 times and greps for broken URLs can be run as follows:

    git clone --recurse-submodules git@github.com:moomop/hugo-8704.git
    cd hugo-8704
    ./test/dup_url_check.py

Example output is given in example_output.txt 