# Chapter 5: Distributed Development

5. [Distributed Development](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#chapter-4-python-libraries)
  - 5.1 [Git Good](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#51-git-good)
  - 5.2 [Secure SSH](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#52-secure-ssh)
  - 5.3 [Compiled Code](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#53-compiled-code)
  - 5.4 [Low Level](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#54-low-level)
  - 5.5 [Make Magic](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#55-make-magic)
  - 5.6 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#56-succinct-summary)

# 5.1 Git Good
Why do we need version control? Writing code takes enough time and energy as is, so why do we need to use additional commands and APIs on top of simply writing our source code? Unfortunately, developers are not perfect and may often need to fix code that does not work first try. Even worse, sometimes you might accidentally introduce new ~~bugs~~features after making code changes and find it difficult to undo all of your changes. These are some issues that may arise when working on a personal project or homework assignment.  

Rather than use a bunch of files named code\_v1.py, code\_v2.py, code\_v3.py, code\_old.py, code\_doesn't\_work.py, code\_copy.py, and code.py it would be nice if you could simply revert some of the changes. Additionally, if you accidentally renamed code.py to code_v3.py, and discover a bug, you would have lost your previous code and have a much more difficult time recovering your previously incomplete but functional code.  

Additionally, in the real world, you will often collaborate on projects with teams of other developers. Since it's unfeasible for every developer to work on the same physical machine, you will need some way for developers to make changes to the code and for multiple developers to work on the same project at the same time. You will also want to be able to keep track of different versions of the code between different developers. "It works on my machine" won't be a valid excuse unless you are Elon Musk and own the company.  

Therefore, it's abundantly clear that it is necessary to have a version control system that can easily track changes in your code over time. Even better, this version control system should allow you to easily revert your code to any save point in your version history. The git version control system is a decentralized and distributed form of version control used widely by developers all around the world. The premise of the git version control system is that your code is composed of various commits, which each submit one or more "diffs", or changes, to their respective files in the source code.  

This format has various advantages. For example, consider a file with millions of lines of code. A version control system that simply kept a copy of each file at each save point would have a large number of redundant memory usage if only a few lines were changed in between commits. Another advantage is the structure of the commits. Each commit has a commit ID, or hash, which is an unique string of characters that represent the commit. This allows the commits to be easily searched for through a two layered file system structure. The first two characters of the commit ID are used as a directory as a layer of indirection. This prevents larger git repositories, such as the Emacs source code, from having too many files in one directory in the ".git" directory, which stores the git history.  

For example, let's examine the ".git" directory of the "Introduction to Software Construction" repository. Since the parent directory of these markdown files was already under git version control, we already have a ".git" file. To initialize a new git repository, you would use the command `git init`.  

```
bash$ git init
Reinitialized existing Git repository in /Users/joebruin/bio_lab/Introduction-to-Software-Construction/.git/
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
bash$ git diff
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
bash$ git add "Chapter 5: Distributed Development.md"
bash$ git status
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

[master cbfc0e4] Added git subchapter to ch5
 1 file changed, 199 insertions(+)
bash$ 
```

To be safe, let's make sure our changes were correctly added. First, let's check our git log to make sure our HEAD is now at our current commit. The HEAD acts like a pointer in the git repository's internal directed acyclic graph structure to indicate which commit should be represented in our current file system.  

```
bash$ git log
commit cbfc0e45e1f42dbc5d2a203e15c983d00ec856a0 (HEAD -> master)
Author: Ning Wang <ningwang1729@gmail.com>
Date:   Sat Dec 31 23:48:15 2022 -0800

    Added git subchapter to ch5

commit eae1343e1afc8cf1f4d563c5b09c7d1f3f6aed3b (origin/master)
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
bash$ 
```

As indicated above, our HEAD is at the current commit. The "HEAD->master" indicates that we are on our master branch. The "origin/master" indicates that the remote github repository is at the previous commit. A remote is a repository that is not local to your machine. The standard name for remotes is usually "origin", and the standard name for the primary branch of the repository is usually "master". This branch should contain the "true" contents of a repository, and is sometimes referred to as "development" or "main". Branches offer a safe way for multiple developers to work on a single repository without worrying about immediately overwriting someone else's work.  

Before branching off to how to create and switch between branches, let's first check that our commit is correct. We can use the `git diff` command on commit IDs or hashes to check differences in contents.  

```
bash$ git diff eae1343e1afc8cf1f4d563c5b09c7d1f3f6aed3b cbfc0e45e1f42dbc5d2a203e15c983d00ec856a0
diff --git a/Chapter 5: Distributed Development.md b/Chapter 5: Distributed Development.md
index af9e952..f610683 100644
--- a/Chapter 5: Distributed Development.md     
+++ b/Chapter 5: Distributed Development.md     
@@ -9,7 +9,206 @@
   - 5.6 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#56-succinct-summary)
 
 # 5.1 Git Good
+Why version control? Writing code takes enough time and energy as is, so why do we need to use additional commands and APIs on top of simply writing our source code? Unfortunately, developers are not perfect and may often need to fix code that does not work first try. Even worse, sometimes you might accidentally introduce new ~~bugs~~features after making code changes and find it difficult to undo all of your changes. These are some issues that may arise when working on a personal project or homework assignment.  
 
+Rather than use a bunch of files named code\_v1.py, code\_v2.py, code\_v3.py, code\_old.py, code\_doesn't\_work.py, code\_copy.py, and code.py it would be nice if you could simply revert some of the changes. Additionally, if you accidentally renamed code.py to code_v3.py, and discover a bug, you would have lost your p
bash$ 
```

As it can be a bit verbose to use entire commit hashes, you can instead use the first four characters of the hashes.  

```
bash$ git diff eae1 cbfc
diff --git a/Chapter 5: Distributed Development.md b/Chapter 5: Distributed Development.md
index af9e952..f610683 100644
--- a/Chapter 5: Distributed Development.md     
+++ b/Chapter 5: Distributed Development.md     
@@ -9,7 +9,206 @@
   - 5.6 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#56-succinct-summary)
 
 # 5.1 Git Good
+Why version control? Writing code takes enough time and energy as is, so why do we need to use additional commands and APIs on top of simply writing our source code? Unfortunately, developers are not perfect and may often need to fix code that does not work first try. Even worse, sometimes you might accidentally introduce new ~~bugs~~features after making code changes and find it difficult to undo all of your changes. These are some issues that may arise when working on a personal project or homework assignment.  
 
+Rather than use a bunch of files named code\_v1.py, code\_v2.py, code\_v3.py, code\_old.py, code\_doesn't\_work.py, code\_copy.py, and code.py it would be nice if you could simply revert some of the changes. Additionally, if you accidentally renamed code.py to code_v3.py, and discover a bug, you would have lost your p
bash$ 
```

Moreover, since it is so common to compare the HEAD commit with previous commits, you can instead simply use HEAD instead of the commit ID.  

```
bash$ git diff eae1..HEAD
diff --git a/Chapter 5: Distributed Development.md b/Chapter 5: Distributed Development.md
index af9e952..f610683 100644
--- a/Chapter 5: Distributed Development.md     
+++ b/Chapter 5: Distributed Development.md     
@@ -9,7 +9,206 @@
   - 5.6 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#56-succinct-summary)
 
 # 5.1 Git Good
+Why version control? Writing code takes enough time and energy as is, so why do we need to use additional commands and APIs on top of simply writing our source code? Unfortunately, developers are not perfect and may often need to fix code that does not work first try. Even worse, sometimes you might accidentally introduce new ~~bugs~~features after making code changes and find it difficult to undo all of your changes. These are some issues that may arise when working on a personal project or homework assignment.  
 
+Rather than use a bunch of files named code\_v1.py, code\_v2.py, code\_v3.py, code\_old.py, code\_doesn't\_work.py, code\_copy.py, and code.py it would be nice if you could simply revert some of the changes. Additionally, if you accidentally renamed code.py to code_v3.py, and discover a bug, you would have lost your p
bash$ 
```

Since it's common to compare the HEAD with the previous commit, this can be further simplified with "HEAD^!".  

```
bash$ git diff HEAD^!
diff --git a/Chapter 5: Distributed Development.md b/Chapter 5: Distributed Development.md
index af9e952..f610683 100644
--- a/Chapter 5: Distributed Development.md     
+++ b/Chapter 5: Distributed Development.md     
@@ -9,7 +9,206 @@
   - 5.6 [Succinct Summary](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/Chapter%205:%20Distributed%20Development.md#56-succinct-summary)
 
 # 5.1 Git Good
+Why version control? Writing code takes enough time and energy as is, so why do we need to use additional commands and APIs on top of simply writing our source code? Unfortunately, developers are not perfect and may often need to fix code that does not work first try. Even worse, sometimes you might accidentally introduce new ~~bugs~~features after making code changes and find it difficult to undo all of your changes. These are some issues that may arise when working on a personal project or homework assignment.  
 
+Rather than use a bunch of files named code\_v1.py, code\_v2.py, code\_v3.py, code\_old.py, code\_doesn't\_work.py, code\_copy.py, and code.py it would be nice if you could simply revert some of the changes. Additionally, if you accidentally renamed code.py to code_v3.py, and discover a bug, you would have lost your p
bash$ 
```

Branching back to branches, you can check the branches currently available using the `git branch` command. If you use `git branch` followed by a branch name, you are creating a new branch with that name that is on par with the current branch. The asterisk '*' indicates which branch is currently active.  

```
bash$ git branch
* master
  temp
bash$ 
```

To checkout a branch, you can use the `git checkout` followed by the branch name. If you want to create a branch and checkout the same branch, you can use `git checkout -b` followed by the branch name. This is functionally the same as using `git branch BRANCHNAME; git checkout BRANCHNAME`. You can also checkout specific commits by specifying the commit ID.  

Finally, you can view which remotes you are connected to with the `git remote` command. To add a remote, you can use `git remote add NAMEOFREMOTE` followed by the URL to the remote repository.  

```
bash$ git remote
origin
bash$ git remote add origin git@github.com:NingWang1729/Introduction-to-Software-Construction.git
bash$ 
```

To push commits to the remote repository, you can use the command `git push origin master`, assuming your remote is named origin and you are pushing to the master branch. If you are working with other people, you should have separate branches to push to and merge branches into master after checking the code. Sometimes, you will encounter merge conflicts, which will require manual resolution. If there is a branch you will often push changes to and pull changes from, you can set git to track that specific branch with the "-u" flag.  

```
bash$ git push -u origin master
Enter passphrase for key '/Users/joebruin/.ssh/id_rsa': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 5.29 KiB | 2.65 MiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:NingWang1729/Introduction-to-Software-Construction.git
   eae1343..cbfc0e4  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

Pulling means to retrieve the changes in the upstream git repository into your local repository. Here, we are up to date with the remote repository since we just pushed our latest commit.  

```
bash$ git pull origin master
Enter passphrase for key '/Users/joebruin/.ssh/id_rsa': 
From github.com:NingWang1729/Introduction-to-Software-Construction
 * branch            master     -> FETCH_HEAD
Already up to date.
bash$ git pull    
Enter passphrase for key '/Users/joebruin/.ssh/id_rsa': 
Already up to date.
bash$ 
```

Finally, you may want to clone a remote repository onto your local machine. All you need to do is to use the `git clone` command followed by the URL of the remote repository.  

```
bash$ mkdir foobar; cd foobar
bash foobar$git clone git@github.com:NingWang1729/Introduction-to-Software-Construction.git
Cloning into 'Introduction-to-Software-Construction'...
Enter passphrase for key '/Users/joebruin/.ssh/id_rsa': 
remote: Enumerating objects: 74, done.
remote: Counting objects: 100% (74/74), done.
remote: Compressing objects: 100% (52/52), done.
remote: Total 74 (delta 45), reused 51 (delta 22), pack-reused 0
Receiving objects: 100% (74/74), 85.46 KiB | 711.00 KiB/s, done.
Resolving deltas: 100% (45/45), done.
bash foobar$ ls
Introduction-to-Software-Construction
bash foobar$ cd ..
bash$ rm -rf foobar
bash$ 
```

# 5.2 Secure SSH
As you may have noticed, the above git commands that were connecting to a remote repository used a Secure Shell (SSH) key rather than a web URL using Hypertext Transport Protocol Secure (HTTPS). SSH keys provide additional cybersecurity, as they can be used for better identifying the user and ensuring the user has permissions to access a remote repository. The SSH key itself is split into two parts: a public key and a private key. The public key is safe for anyone to have acess to in order to verify that you are who you claim to be. In contrast, the private key is known only to the user. This acts like a lock and key mechanism. The public keys are similar to locks that anyone can have access to, but only the user has the private key, which can unlock the locks.  

The simplest way to create an SSH key is to use the command `ssh-keygen`. By default, this uses the Rivest–Shamir–Adleman (RSA) algorithm.  

```
bash$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/cs111/.ssh/id_rsa): /home/cs111/.ssh/id_rsa
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/cs111/.ssh/id_rsa
Your public key has been saved in /home/cs111/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:OGv4uP9vMQRLeXSl2jED4pxakXHWwVwZcLlEKPNEQQ4 cs111@cs111
The key's randomart image is:
+---[RSA 3072]----+
|        +=E*BO*+ |
|       o=*+=*o+  |
|       .=+ =*. . |
|       +. .o.+.  |
|      + S.. .    |
|     . o  o      |
|    . o    o     |
|     +    .      |
|    ooo..o.      |
+----[SHA256]-----+
bash$ 
```

Now that you have generated a new SSH key, you will want to add it to wherever you are storing your remote repositories. For GitHub, you can add an SSH key to your account [here](https://github.com/settings/ssh/new). You will need to copy over the contents of your public key. Your public key will have the same file name as your private key, with a ".pub" suffix appended at the end.  

```
bash$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQD0mkLgAwS9eZ6NjLBvErdA4Gg4mJykNyXO6EvVOJ2yYAAhk6yc3oEbpWYd499JSfq29L5TQvA1qitljWLe+u/u2ibmkYyb4yl5bP9jclBbiLayUKsipbK9fsIScleStEYcOvhRttaH1IfihCoc0mgnhVlVzqhzKKqR8wNVw2Tav4nUzpXA5VOW5Yr4unNMWZ885uBQYjf6aptSJ+z8uSJPXKwUhrbDoXpzAEO8qhf6h7DZ13KDYyqvlR8lrGm0Uft0UYnx7is/QqwmT8H4Jc6YWoFzq6wFdfs61lxEgAyBXFHSBcOzaAAbtaZ7Qd46y37P3lDvqNkNqccps1I6igLPpKirPGtjCKX/J+qI0pQdgAnMAWQkE5U0StoU0x7AFlqX7JNQueaR3Vl+NytlK4qT9wiXMPNHwn9h4HpguuFUuS3YrFveeM8+XpMp9ZLXOmnZaQLKmOAiIa5AOlZ8f/OGBibJlO4w0jax8Jg8wn8HfnboG7RQcwedtawZcwzr5yM= cs111@cs11
```

Additionally, you can add a comment to your SSH key for future reference.  

```
bash$ ssh-keygen -C "Fancy comment."
Generating public/private rsa key pair.
Enter file in which to save the key (/home/cs111/.ssh/id_rsa): /home/cs111/.ssh/id_rsa
/home/cs111/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/cs111/.ssh/id_rsa
Your public key has been saved in /home/cs111/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:gKF0Dx9Fsu1UWM4IAREweUe3dd5ZABaF01bC5AmWXWg Fancy comment.
The key's randomart image is:
+---[RSA 3072]----+
|  +oB=*++o+ B@==+|
| ..+.*.B.B =++E= |
|  ....= = o .+=  |
|       +         |
|        S        |
|                 |
|                 |
|                 |
|                 |
+----[SHA256]-----+
bash$ cat ~/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCfVeqh+aqv6uf+VNL6KBbN13cncQ0oQhqa5FVbTgzOVAxfvnOvsVgY1qLaZXZZxoGLADi66ez5HybkQ1/6hXrWEsBaK57FOKw512/LyC1eloE/J9EuyJIQW54pJrpMeODapZKkmD51qY7Eq/FEkuKL1x2LkxLgGFDR4cirIBTyeflDGZ0splzLVHSZVy44ODX7MVi+EUzsWMGjoSNtEprxOuAvq4OtW45sAPmAEcOIN4H1zh0oN9p+wYL4ZkSeBL34CwwpOp4Fk7OOVspJKAV23unDSOqxuRRaIqQQaCOjtp5c0fKSwBa42HeduYQ9PtUnBMFu1YX5zLqrXx1NCryc+DttB/9Jd63K7L+LWrbNUrQtk+nc62sV+STw5mEn11t83BOMBDolKFL4N4IaVCcyoAZdtiPfgFI2mnUjJjEiKL8Szdj1Ylm7DP+avu2dJWbnsNQXVmtdQiIQiZRjDTUQ1RHKrKy06ZYwH7fjzJolnnFiM/o/ZAGG2RnUKDpaxIU= Fancy comment.
bash$ 
```

Once this is finished, you can view your saved SSH keys [here](https://github.com/settings/keys). While it is safe to share public keys, do not share your private keys, as they can be used to impersonate you.  

# 5.3 Compiled Code


# 5.4 Low Level


# 5.5 Make Magic


# 5.6 Succinct Summary


#### [Return to Main Table of Contents](https://github.com/NingWang1729/Introduction-to-Software-Construction/blob/master/README.md#table-of-contents)

Copyright © 2022 Ning Wang  
[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
