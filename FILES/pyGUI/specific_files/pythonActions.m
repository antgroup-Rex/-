% https://www.mathworks.com/help/matlab/matlab_external/call-methods-on-python-variables.html
P = py.sys.path
methods(P)
methods 'handle' 
py.help('list.append')

append(P, pwd)

disp(P)
py.len(P)
% https://www.mathworks.com/help/matlab/matlab_external/call-python-eval-function.html
workspace = py.dict(pyargs('x',1,'y',6))
res = py.eval('x+y',workspace)
