# Chapter 5: Distributed Development

5. [Distributed Development](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#chapter-4-python-libraries)
  - 5.1 [Git Good](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#51-git-good)
  - 5.2 [Secure SSH](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#52-secure-ssh)
  - 5.3 [Compiled Code](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#53-compiled-code)
  - 5.4 [Low Level](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#54-low-level)
  - 5.5 [Make Magic](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#55-make-magic)
  - 5.6 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#56-succinct-summary)

# 5.1 Git Good
Why version control? Writing code takes enough time and energy as is, so why do we need to use additional commands and APIs on top of simply writing our source code? Unfortunately, developers are not perfect and may often need to fix code that does not work first try. Even worse, sometimes you might accidentally introduce new ~~bugs~~features after making code changes and find it difficult to undo all of your changes. These are some issues that may arise when working on a personal project or homework assignment.  

Rather than use a bunch of files named code\_v1.py, code\_v2.py, code\_v3.py, code\_old.py, code\_doesn't\_work.py, code\_copy.py, and code.py it would be nice if you could simply revert some of the changes. Additionally, if you accidentally renamed code.py to code_v3.py, and discover a bug, you would have lost your previous code and have a much more difficult time recovering your previously incomplete but functional code.  

Additionally, in the real world, you will often collaborate on projects with teams of other developers. Since it's unfeasible for every developer to work on the same physical machine, you will need some way for developers to make changes to the code and for multiple developers to work on the same project at the same time. You will also want to be able to keep track of different versions of the code between different developers. "It works on my machine" won't be a valid excuse unless you are Elon Musk and own the company.  

Therefore, it's abundantly clear that it is necessary to have a version control system that can easily track changes in your code over time. Even better, this version control system should allow you to easily revert your code to any save point in your version history. The git version control system is a decentralized and distributed form of version control used widely by developers all around the world. The premise of the git version control system is that your code is composed of various commits, which each submit one or more "diffs", or changes, to their respective files in the source code.  

This format has various advantages. For example, consider a file with millions of lines of code. A version control system that simply kept a copy of each file at each save point would have a large number of redundant memory usage if only a few lines were changed in between commits. Another advantage is the structure of the commits. Each commit has a commit ID, or hash, which is an unique string of characters that represent the commit. This allows the commits to be easily searched for through a two layered file system structure. The first two characters of the commit ID are used as a directory as a layer of indirection. This prevents larger git repositories, such as the Emacs source code, from having too many files in one directory in the ".git" directory, which stores the git history.  

For example, let's examine the ".git" directory of the "Introduction to Software Construction" repository. Since the parent directory of these markdown files was already under git version control, we already have a ".git" file. To initialize a new git repository, you would use the command `git init`.  

```
bash$ git init
Reinitialized existing Git repository in /Users/ningwang/bio_lab/Introduction-to-Software-Construction/.git/
bash$ cd .git
bash .git$ ls
COMMIT_EDITMSG	ORIG_HEAD	description	info		refs
FETCH_HEAD	branches	hooks		logs
HEAD		config		index		objects
bash .git$ 
```

Inside the ".git" directory, we can look at the objects, which contain the git objects that represent each commit. Having two character sub-directory names offers a balance between having too many sub-directories in the objects directory and not having enough indirection for too many commits in each sub-directory.  

```
bash .git$ cd objects
bash objects $ ls
06	13	29	3a	66	7c	af	c9	eb	info
08	14	2b	3b	68	81	b0	ce	ed	pack
0a	16	30	43	6c	86	b6	cf	f1
0c	19	31	62	70	87	b7	d5	f5
0d	1c	32	63	73	8b	c1	df	f6
0f	1f	35	64	76	96	c2	e2	f8
11	27	36	65	7a	ad	c5	ea	f9
bash objects$ cd 2b
bash 2b$ ls
2f169b25c6f350810ae884ebeae6517dec20d1
bash 2b$ 
```

Each commit should also have a commit message to describe the change. We can examine the commit history in a number of ways. For example, we can examine the internal contents of the ".git" repository to check each commit. Inside the logs sub-directory, we see a "HEAD" file. This contains the commits in the git version control history up to the most recent and currently active commit.  

```
bash 2b$ cd ../..
bash .git$ cd logs 
bash logs$ ls
HEAD	refs
bash logs$ cat HEAD | head
0000000000000000000000000000000000000000 f848da7c52b7bb022eaa4fe45dda700ea293f4a7 Ning Wang <ningwang1729@gmail.com> 1661739803 -0700	commit (initial): Initial commit: Updated README.md, Chapters 1-3, References, License
f848da7c52b7bb022eaa4fe45dda700ea293f4a7 30e87424dc7ea997098698b1ed7d3d8dcd4fb375 Ning Wang <ningwang1729@gmail.com> 1662452496 -0700	commit: Add ch4.1 and demonstration scripts
30e87424dc7ea997098698b1ed7d3d8dcd4fb375 ced5600fbf60d34fc8ee76812d8af3b88f993ed4 Ning Wang <ningwang1729@gmail.com> 1662452745 -0700	commit: update table of contents and copyright
ced5600fbf60d34fc8ee76812d8af3b88f993ed4 43c8b88ce85c4642bcf988419ccb67fa2e8e3297 Ning Wang <ningwang1729@gmail.com> 1662452856 -0700	commit: fix broken link
43c8b88ce85c4642bcf988419ccb67fa2e8e3297 c10e2f23c495dd99e9aafe81eac6d6fd7d2c43da Ning Wang <ningwang1729@gmail.com> 1662453251 -0700	commit: update References for ch4.1
c10e2f23c495dd99e9aafe81eac6d6fd7d2c43da edf2e5c5ae2d48801d3573e29fc720160db1361f Ning Wang <ningwang1729@gmail.com> 1663544670 -0700	commit: Added Logging module to ch4
edf2e5c5ae2d48801d3573e29fc720160db1361f 0c514892b6c647f325a618aac17347d974456510 Ning Wang <ningwang1729@gmail.com> 1663548268 -0700	commit: updated pdb for ch4 and temperature_conversion.py script
0c514892b6c647f325a618aac17347d974456510 0c514892b6c647f325a618aac17347d974456510 Ning Wang <ningwang1729@gmail.com> 1663548489 -0700	reset: moving to head
0c514892b6c647f325a618aac17347d974456510 edf2e5c5ae2d48801d3573e29fc720160db1361f Ning Wang <ningwang1729@gmail.com> 1663548513 -0700	reset: moving to edf2e5c5ae2d48801d3573e29fc720160db1361f
edf2e5c5ae2d48801d3573e29fc720160db1361f f9f44928e086f6bd52d41a2241de3397358ed3fa Ning Wang <ningwang1729@gmail.com> 1663548584 -0700	commit: update ch4 with pdb and temperature_conversion.py
bash logs$ cat HEAD | tail
7a6fae0e23eab24e4f36d6eec7e68d239a8340fa 321eed3081bcf62b7b5c9f777e6fa684e042865f Ning Wang <ningwang1729@gmail.com> 1670829091 -0800	commit: Update References for Ch4
321eed3081bcf62b7b5c9f777e6fa684e042865f 81acf5d6de368058c875c97a50b0d49168f47f6e Ning Wang <ningwang1729@gmail.com> 1672477434 -0800	commit: finish Ch4
81acf5d6de368058c875c97a50b0d49168f47f6e 76f017062c953831eb508759af9c01327b4c93f5 Ning Wang <ningwang1729@gmail.com> 1672478370 -0800	commit: Update Ch1 with arrays and basic functions
76f017062c953831eb508759af9c01327b4c93f5 eb45510e2da4eb6bfc6883bbf7b4b6aeb74c411c Ning Wang <ningwang1729@gmail.com> 1672479517 -0800	commit: minor grammar fix
eb45510e2da4eb6bfc6883bbf7b4b6aeb74c411c 31c10ebc4581704c4057afd5aeb8f4da11b071f9 Ning Wang <ningwang1729@gmail.com> 1672553596 -0800	commit: fix ch4 link, add ch5 table of contents
31c10ebc4581704c4057afd5aeb8f4da11b071f9 c22667cc840f69e2f50106f8ea891ced574a6247 Ning Wang <ningwang1729@gmail.com> 1672553776 -0800	commit: reformat Table of Contents (add ch5)
c22667cc840f69e2f50106f8ea891ced574a6247 369c25730b12adadcf94d6692cf35df6c79064cf Ning Wang <ningwang1729@gmail.com> 1672554068 -0800	commit: reformat Table of Contents and headers
369c25730b12adadcf94d6692cf35df6c79064cf f9e06ca923e5bfaa339078d93cd5142e6e9299e1 Ning Wang <ningwang1729@gmail.com> 1672554150 -0800	commit: reformat Table of Contents
f9e06ca923e5bfaa339078d93cd5142e6e9299e1 14f17b09f781a61b12b363b91539cc4ac54b1eb5 Ning Wang <ningwang1729@gmail.com> 1672554441 -0800	commit: fix table of contents link
14f17b09f781a61b12b363b91539cc4ac54b1eb5 eae1343e1afc8cf1f4d563c5b09c7d1f3f6aed3b Ning Wang <ningwang1729@gmail.com> 1672554478 -0800	commit: fix table of contents link
bash logs$ 
```

An easier way to view the logs of the commit history interactively is to simply use the git log command. This command will work from anywhere within a git repository. As usual, to exit the interactive terminal command, you can use the "q" key to quit from the interactive command.  

```
bash logs$ cd ../..
bash$ git log
commit eae1343e1afc8cf1f4d563c5b09c7d1f3f6aed3b (HEAD -> master, origin/master)
Author: Ning Wang <ningwang1729@gmail.com>
Date:   Sat Dec 31 22:27:58 2022 -0800

    fix table of contents link

commit 14f17b09f781a61b12b363b91539cc4ac54b1eb5
Author: Ning Wang <ningwang1729@gmail.com>
Date:   Sat Dec 31 22:27:21 2022 -0800

    fix table of contents link

commit f9e06ca923e5bfaa339078d93cd5142e6e9299e1
Author: Ning Wang <ningwang1729@gmail.com>
Date:   Sat Dec 31 22:22:30 2022 -0800

    reformat Table of Contents

commit 369c25730b12adadcf94d6692cf35df6c79064cf
Author: Ning Wang <ningwang1729@gmail.com>
Date:   Sat Dec 31 22:21:08 2022 -0800

    reformat Table of Contents and headers
bash$ 
```

In each commit, there is a commit ID, or hash, along with the author (name and email) and timestamp of the commit date. The commit message allows the user to view a summary of which changes were made by the commit.  

Before making any commit, you should first check the status of your git repository. This allows you to make sure you have the correct changes in your staging area. To check the status of your git repository, use the `git status` command.  

```
bash$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   Chapter 5: Distributed Development.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	#Chapter 5: Distributed Development.md#
	.#Chapter 5: Distributed Development.md
	foo.md
	readme.copy.md

no changes added to commit (use "git add" and/or "git commit -a")
bash$ 
```

As indicated by the above output, we have some changes in this current file, "Chapter 5: Distributed Development.md" that have not been staged. A staged file is a file that has changes that you will commit upon making your next commit. To stage the file, you can use the command `git add` followed by the name of the file. In general, it is recommended to not have any spaces in your file names. However, if you do happen to have such spaces, you can either use the backslash '\' to escape the spaces or to enclose the entire name within quotation marks "".  

However, it is recommended that you double check that the changes you intend to stage are the changes you expect to be made. To check the difference between the current file and the previous instance of the file in the previous commit, you can use the `git diff` command, followed by the name of the file. This is an interactive command, so you can use 'q' to exit. If you wanted to jump to the end of the "diff", you can use the "G" vim keybinding (SHIFT + 'g').  

```
ningwang@Nings-MacBook-Pro Introduction-to-Software-Construction % git diff
diff --git a/Chapter 5: Distributed Development.md b/Chapter 5: Distributed Development.md
index af9e952..453eccf 100644
--- a/Chapter 5: Distributed Development.md     
+++ b/Chapter 5: Distributed Development.md     
@@ -9,6 +9,135 @@
   - 5.6 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#56-succinct-summary)
 
 # 5.1 Git Good
+Why version control? Writing code takes enough time and energy as is, so why do we need to use additional commands and APIs on top of simply writing our source code? Unfortunately, developers are not perfect and may often need to fix code that does not work first try. Even worse, sometimes you might accidentally introduce new ~~bugs~~features after making code changes and find it difficult to undo all of your changes. These are some issues that may arise when working on a personal project or homework assignment.  
+
+Rather than use a bunch of files named code\_v1.py, code\_v2.py, code\_v3.py, code\_old.py, code\_doesn't\_work.py, code\_copy.py, and code.py it would be nice if you could simply revert some of the changes. Additionally, if you accidentally renamed code.py to code_v3.py, and discover a bug, you would have lost your p...skipping...
+bash$ git status
+On branch master
+Your branch is up to date with 'origin/master'.
+
+Changes not staged for commit:
+  (use "git add <file>..." to update what will be committed)
+  (use "git restore <file>..." to discard changes in working directory)
+       modified:   Chapter 5: Distributed Development.md
+
+Untracked files:
+  (use "git add <file>..." to include in what will be committed)
+       #Chapter 5: Distributed Development.md#
+       .#Chapter 5: Distributed Development.md
+       foo.md
+       readme.copy.md
+
+no changes added to commit (use "git add" and/or "git commit -a")
+bash$ 
+```
+
 
 
 # 5.2 Secure SSH
bash$ 
```

Since these are the changes we wanted to make, we can now use `git add` followed by the file name. Alternatively, if you wanted to add all changes not staged for commit, you can use `git add -u` to add all tracked files. Untracked files, in contrast, are "hidden" away from the git version control system. You may want to not track some files if they are not ready to be added, but if you lose your data, then you will not be able to retrieve the untracked files through git version control by reverting to an earlier commit.  

```
bash$ ningwang@Nings-MacBook-Pro Introduction-to-Software-Construction % git add "Chapter 5: Distributed Development.md"
ningwang@Nings-MacBook-Pro Introduction-to-Software-Construction % git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   Chapter 5: Distributed Development.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	#Chapter 5: Distributed Development.md#
	.#Chapter 5: Distributed Development.md
	foo.md
	readme.copy.md

bash$ 
```

Now that we have our saved changes in our staging area, we can finally make a commit. As you may have guessed, we can use the `git commit` command to commit our changes to the git repository. To add a commit message, we can add "-m" flag followed by the commit message so we can more easily recall what changes we made and why we made them when we review our git history.  

```
bash$ git commit -m "Added git subchapter to ch5"
bash$ 
```

# 5.2 Secure SSH


# 5.3 Compiled Code


# 5.4 Low Level


# 5.5 Make Magic


# 5.6 Succinct Summary


#### [Return to Main Table of Contents](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/README.md#table-of-contents)

Copyright © 2022 Ning Wang  
[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
