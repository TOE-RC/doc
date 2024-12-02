## 常规操作

开始前我们需要先设置提交的用户信息，包括用户名和邮箱：

```bash
$ git config --global user.name 'name'
$ git config --global user.email test@test.com
```

### 创建版本库

首先，打开终端或命令行界面，进入要创建版本库的目录下。

接着，使用以下命令初始化一个空的 Git 仓库：

```bash
git init
```

然后，将需要管理的文件添加到暂存区：

```bash
git add
```

你也可以使用以下命令一次性将所有变更添加到暂存区：

```bash
git add .
```

接下来，提交暂存区中的变更到本地仓库，并添加一个描述信息：

```bash
git commit -m '第一次版本提交'
```

现在，你已经成功地创建了一个版本库。你可以使用其他 Git 命令来管理它，例如：

> git status：查看当前工作区和暂存区的状态。
> git log：查看提交记录。
> git branch：管理分支。
> git remote：管理远程仓库。

## 远程仓库

### 如何添加远程仓库

要将本地代码库连接到远程仓库，可以使用以下git命令：

首先，将本地代码库初始化为Git仓库（如果尚未完成）：

```bash
git init
```

添加远程仓库的URL，其中<remote-name>是自定义名称，<remote-url>是远程仓库的URL：

```bash
git remote add <remote-name> <remote-url>
```

可以使用以下命令确认远程仓库是否已成功添加：

```bash
git remote -v
```

此后，您就可以使用 `git push`命令将代码推送到远程仓库，或使用 `git pull`命令从远程仓库拉取代码。

### 从远程库克隆

要从远程仓库克隆代码到本地，可以使用以下git命令：

```bash
git clone <remote-url>
```

其中<remote-url>是远程仓库的URL。执行此命令后，Git将在当前目录下创建一个新目录，其中包含克隆的代码库副本。如果想指定不同的目录名，可以将目录名作为可选参数添加到命令中：

```bash
git clone <remote-url> <directory-name>
```

## 创建与合并分支

创建一个新的分支可以使用以下命令：

```bash
git branch <branch_name>
```

这将在当前所在的提交上创建一个名为 <branch_name> 的新分支。

要切换到新创建的分支，可以使用以下命令：

```bash
git checkout <branch_name>
```

创建并立即切换到该分支，可以使用以下命令：

```bash
git checkout -b <branch_name>
```

合并分支可以使用以下命令：

```bash
git merge <branch_name>
```

这将将 <branch_name> 分支中的更改合并到当前分支。

## 推送分支

在 Git 中，推送分支指将本地的分支提交到远程仓库中，使得其他团队成员可以访问和获取该分支的代码。以下是在 Git 中推送分支的一些常用命令：

推送当前分支到远程仓库，并与远程分支关联：

```bash
git push -u origin <branch-name>
```

推送当前分支到远程仓库，并与远程分支合并：

```bash
git push origin <branch-name>
```

强制推送当前分支到远程仓库：

```bash
git push -f origin <branch-name>
```

删除远程分支：

```bash
git push origin :<branch-name>
```

或

```bash
git push --delete origin <branch-name>
```

在推送分支时，通常会遇到冲突等问题。如果发生冲突，需要先解决冲突，然后再进行推送。

## 处理冲突

当两个分支上的代码修改了同一部分，并且尝试将这两个分支合并时，就会发生代码冲突。Git提供了以下步骤来解决冲突：

运行 `git status` 命令查看哪些文件包含冲突。
编辑有冲突的文件，手动解决文件中的冲突。
对编辑后的文件进行 `git add`，标记为已解决冲突的文件。
使用 `git commit` 提交更改，Git 会自动生成一个合并提交，其中包含各自分支中的更改。
注意：在解决冲突前，最好先备份当前的代码状态，以免不小心破坏代码库。另外，在处理冲突之前，可以通过运行 `git diff` 命令来查看冲突的源代码，以便更好地理解要解决的问题。

### 分支管理策略

在 Git 中，常见的分支管理策略包括以下几个方面：

+ 主分支：主分支通常是最稳定的分支，用于发布生产版本。在 Git 中，主分支通常是 master 分支或者 main 分支。
+ 开发分支：开发分支通常从主分支派生而来，在其上进行新功能或修复错误的开发。在 Git 中，通常使用 develop 分支作为开发分支。
+ 特性分支：特性分支是为了开发单独的功能而创建的分支。这些分支通常从开发分支派生而来，并在实现目标后被合并回开发分支。在 Git 中，通常使用 feature/ 分支命名约定来表示特性分支。
+ 发布分支：发布分支是用于准备发布版本的分支，通常从主分支派生而来。这些分支应该包含与发布相关的所有更改，并且应该经过全面测试和审核后再合并回主分支。在 Git 中，通常使用 release/ 分支命名约定来表示发布分支。
+ 热修复分支：热修复分支通常用于快速修复紧急问题，例如安全漏洞或崩溃。这些分支通常从主分支派生而来，并且只包含必要的更改。在 Git 中，通常使用 hotfix/ 分支命名约定来表示热修复分支。

## 具体操作

### 克隆仓库

```bash
git clone git@github.com:TOE-RC/robotmaster-c.git
git clone <remote-url>
```

![https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_5f052876d9b219f42b9a86fb47c60eac.png](https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_5f052876d9b219f42b9a86fb47c60eac.png)

### 提交仓库

在本地更改并且保存后，使用这条命令一次性将所有变更添加到暂存区

```bash
git add .
```

提交暂存区中的变更到本地仓库，并添加一个描述信息：

```bash
git commit -m '第一次版本提交'
```

提交到远程仓库

```bash
git push
```

![https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_71bdf1e5c87f0be8a689fcfc43f8b11c.png](https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_71bdf1e5c87f0be8a689fcfc43f8b11c.png)

### 处理冲突

![https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_7250aa9512338a42987cd48ae6584453.png](https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_7250aa9512338a42987cd48ae6584453.png)

在你提交之前假设有其他人提交了新的版本，这时候提交就会出现冲突错误

![https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_cc8aa3ad57e9d7df94390d124267cfdb.png](https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_cc8aa3ad57e9d7df94390d124267cfdb.png)

建议使用VSCode自带的插件

![https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_13388c15ab1f627389c004600f703318.png](https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_13388c15ab1f627389c004600f703318.png)

### 覆盖仓库

![https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_2e3cee40df1501f13914050a36fe0e26.png](https://cdn.ziyourufeng.eu.org/51hhh/img_bed/main/img/2024/11_21/image_2e3cee40df1501f13914050a36fe0e26.png)

本地初始化Git文件夹 `git init`，绑定远程仓库 `git remote add robotmaster-c git@github.com:TOE-RC/robotmaster-c.git`，检测仓库是否成功添加 `git remote -v`。

这里 `git pull`出现了错误，提示如果你想要拉取并合并特定的分支，你需要指定远程仓库和分支名 `git pull remote branch`，或者为当前分支设置跟踪信息，之后，你就可以简单地使用 `git pull` 来拉取最新的代码，而不需要每次都指定远程仓库和分支。

首先先建立本地分支进行第一次提交

```bash
git add .
git commit -m "Initial commit"
```

获取远程仓库的所有分支信息：

```bash
git fetch
```

设置跟踪远程 `main` 分支

```bash
git branch --set-upstream-to=robotmaster-c/main master
git branch --set-upstream-to=仓库名/仓库分支 本地分支
```

此时即可 `git pull --allow-unrelated-histories`