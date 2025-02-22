Name:		python-tabulate
Version:	0.9.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/tabulate/tabulate-%{version}.tar.gz
Summary:	Pretty-print tabular data
URL:		https://pypi.org/project/tabulate/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Pretty-print tabular data

%files
%{_bindir}/tabulate
%{py_sitedir}/tabulate
%{py_sitedir}/tabulate-*.*-info
