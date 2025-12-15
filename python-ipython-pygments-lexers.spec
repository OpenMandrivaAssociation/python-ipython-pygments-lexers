Name:		python-ipython-pygments-lexers
Version:	1.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/i/ipython_pygments_lexers/ipython_pygments_lexers-%{version}.tar.gz
Summary:	Defines a variety of Pygments lexers for highlighting IPython code.
URL:		https://pypi.org/project/ipython-pygments-lexers/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Defines a variety of Pygments lexers for highlighting IPython code.

%files
%{py_sitedir}/__pycache__/*
%{py_sitedir}/ipython_pygments_lexers.py
%{py_sitedir}/ipython_pygments_lexers-*.*-info
