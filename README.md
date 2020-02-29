# PyNovelDoc

Gal, Novel DSL Impl.

## Syntax

- [x] Say
- [x] Let Flag
- [x] Choice
- [x] Global Novel
- [x] Create A Sub Novel
- [x] Comments
- [x] Command
- [ ] Inject Code
- [ ] Camera Move
- [ ] Model Action

### Say

``` gal
Say 「 Hello World 」
lfkdsk [ status ] Say 「 Hello World 」
```

example:

```gal
lfkdsk [Angry] Say 「 I'm Angry 」# change status pic with status.
```

### Let Flag

``` gal
SET VAR_NAME = VALUE
```

### Command 

``` gal
> COMMAND ARGS
```

example:
```gal
> Music 异邦人
> Background 体育仓库
```

### Inject Code

```gal

--- [Python or Other Script Type]
# Write Python Code.
---

```

### Choice (Jump)

Choice Jump Novel.
```gal
- [Choice 1] to Novel 1
- [Choice 2] to Novel 2
- [Choice 3] to Novel 3
```

Choice change flag.

```gal
- [Choice 1] to lambda 1
- [Choice 2] to lambda 2
- [Choice 3] to lambda 3
```


### Camera Move

```gal
# bind camera
+ { A : [ x, y, scale ] , B : [x, y, scale]}
# unbind camera
- [A , B]
```

### Chapter 

```gal
=== Chapter 1 ===
```

show empty with text chapter x

### Model Action

```gal
[A] -> Action
```

example:

```gal
[someone] -> reset dresses
```

### Comments

```gal
# its a comment
```

may show this in debugger mode or toolkit window.

### Create A Novel

```gal
Start <Novel Name>
# other stmts. 
End <Novel>
```

### Global Novel

``` gal
NOVEL_START
# Novel Script
NOVEL_END
```
