# Automated Reports
## Coverage Report
text
Name                     Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------
cli/cli.py                 131     41     50     13    66%   23-26, 43-46, 92-93, 105-106, 109-110, 114-123, 128-129, 132-136, 154-155, 158-176, 180
core/__init__.py             0      0      0      0   100%
core/backgammongame.py     199      1    104      1    99%   210->exit, 357
core/board.py               69      0     34      0   100%
core/checker.py             16      0      2      0   100%
core/dice.py                14      0      2      0   100%
core/exceptions.py           4      0      0      0   100%
core/player.py              10      0      0      0   100%
--------------------------------------------------------------------
TOTAL                      443     42    192     14    90%


## Pylint Report
text
************* Module core.checker
core/checker.py:16:0: C0303: Trailing whitespace (trailing-whitespace)
core/checker.py:26:0: C0303: Trailing whitespace (trailing-whitespace)
core/checker.py:30:0: C0303: Trailing whitespace (trailing-whitespace)
core/checker.py:33:0: C0304: Final newline missing (missing-final-newline)
core/checker.py:33:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
core/checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/checker.py:2:0: C0115: Missing class docstring (missing-class-docstring)
************* Module core.backgammongame
core/backgammongame.py:55:0: C0301: Line too long (113/100) (line-too-long)
core/backgammongame.py:84:0: C0301: Line too long (132/100) (line-too-long)
core/backgammongame.py:95:0: C0301: Line too long (102/100) (line-too-long)
core/backgammongame.py:144:0: C0301: Line too long (149/100) (line-too-long)
core/backgammongame.py:146:0: C0303: Trailing whitespace (trailing-whitespace)
core/backgammongame.py:149:0: C0301: Line too long (144/100) (line-too-long)
core/backgammongame.py:239:0: C0301: Line too long (140/100) (line-too-long)
core/backgammongame.py:243:0: C0301: Line too long (103/100) (line-too-long)
core/backgammongame.py:254:0: C0301: Line too long (106/100) (line-too-long)
core/backgammongame.py:262:0: C0301: Line too long (139/100) (line-too-long)
core/backgammongame.py:266:0: C0301: Line too long (103/100) (line-too-long)
core/backgammongame.py:277:0: C0301: Line too long (106/100) (line-too-long)
core/backgammongame.py:291:23: C0303: Trailing whitespace (trailing-whitespace)
core/backgammongame.py:298:20: C0303: Trailing whitespace (trailing-whitespace)
core/backgammongame.py:307:39: C0303: Trailing whitespace (trailing-whitespace)
core/backgammongame.py:309:39: C0303: Trailing whitespace (trailing-whitespace)
core/backgammongame.py:311:39: C0303: Trailing whitespace (trailing-whitespace)
core/backgammongame.py:313:45: C0303: Trailing whitespace (trailing-whitespace)
core/backgammongame.py:315:25: C0303: Trailing whitespace (trailing-whitespace)
core/backgammongame.py:152:4: R0912: Too many branches (13/12) (too-many-branches)
core/backgammongame.py:228:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
core/backgammongame.py:228:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
core/backgammongame.py:228:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
core/backgammongame.py:228:8: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
core/backgammongame.py:213:4: R0912: Too many branches (16/12) (too-many-branches)
core/backgammongame.py:8:0: R0904: Too many public methods (22/20) (too-many-public-methods)
************* Module core.board
core/board.py:71:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:102:48: E1135: Value 'casilla' doesn't support membership test (unsupported-membership-test)
************* Module cli.cli
cli/cli.py:34:0: C0303: Trailing whitespace (trailing-whitespace)
cli/cli.py:101:0: C0303: Trailing whitespace (trailing-whitespace)
cli/cli.py:53:0: R0914: Too many local variables (17/15) (too-many-locals)
cli/cli.py:175:11: W0718: Catching too general exception Exception (broad-exception-caught)
cli/cli.py:65:4: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
cli/cli.py:65:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
cli/cli.py:53:0: R0912: Too many branches (21/12) (too-many-branches)
cli/cli.py:53:0: R0915: Too many statements (87/50) (too-many-statements)
cli/cli.py:65:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
************* Module pygame_ui.events
pygame_ui/events.py:62:19: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module pygame_ui.iboard
pygame_ui/iboard.py:6:0: R0902: Too many instance attributes (33/7) (too-many-instance-attributes)
pygame_ui/iboard.py:104:4: R0913: Too many arguments (8/5) (too-many-arguments)
pygame_ui/iboard.py:104:4: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
pygame_ui/iboard.py:118:4: R0913: Too many arguments (8/5) (too-many-arguments)
pygame_ui/iboard.py:118:4: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
pygame_ui/iboard.py:162:4: R0913: Too many arguments (6/5) (too-many-arguments)
pygame_ui/iboard.py:162:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
pygame_ui/iboard.py:174:4: R0913: Too many arguments (6/5) (too-many-arguments)
pygame_ui/iboard.py:174:4: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
pygame_ui/iboard.py:174:4: R0914: Too many local variables (35/15) (too-many-locals)
pygame_ui/iboard.py:174:4: R0912: Too many branches (16/12) (too-many-branches)
pygame_ui/iboard.py:174:4: R0915: Too many statements (67/50) (too-many-statements)
pygame_ui/iboard.py:256:35: W0612: Unused variable 'rect' (unused-variable)
pygame_ui/iboard.py:336:16: W0612: Unused variable 'origen' (unused-variable)
pygame_ui/iboard.py:377:25: W0612: Unused variable 'x' (unused-variable)
pygame_ui/iboard.py:377:28: W0612: Unused variable 'y' (unused-variable)
pygame_ui/iboard.py:377:31: W0612: Unused variable 'ha' (unused-variable)

-----------------------------------
Your code has been rated at 9.16/10



