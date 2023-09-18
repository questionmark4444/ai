ifeq ($(OS),Windows_NT)
    cl -fPIC -shared -o my_functions.so my_functions.c -Os
    python3 -m compileall ai.py
    move __pycache__/ai.cpython-310.pyc ai.cpython-310.pyc
    python3 -m compileall saver.py
    move __pycache__/saver.cpython-310.pyc saver.cpython-310.pyc
else
    ifeq ($(UNAME_S),Linux)
        gcc -fPIC -shared -o my_functions.so my_functions.c -Os
        python3 -m compileall ai.py
        mv __pycache__/ai.cpython-310.pyc ai.cpython-310.pyc
        chmod +x ai.cpython-310.pyc
        python3 -m compileall saver.py
        mv __pycache__/saver.cpython-310.pyc saver.cpython-310.pyc
        chmod +x saver.cpython-310.pyc
    endif
endif

