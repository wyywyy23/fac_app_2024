# Faculty application materials all in one place

---

## Initialize the project folder

```bash
git clone https://github.com/wyywyy23/fac_app_2024.git
```

or, if you prefer [ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh):

```bash
git clone git@github.com:wyywyy23/fac_app_2024.git
```

Then, initialize the common submodules by running:

```bash
cd fac_app_2024
git submodule update --init --recursive
```

You can check out the latest development branch with:

```bash
git submodule foreach --recursive git checkout master
```

or, merge updates (if any) later on with:

```bash
git submodule update --remote --merge
```

## Make

You only need to supply your own signature file in folder `2_signature/` as `sig.pdf`. Then, run:

```bash
make
```

To clean up the folder, run:

```bash
make clean-cache
```

to remove all temporary files, or:

```bash
make clean
```

to remove all generated PDFs as well.

---

# Happy applying!
