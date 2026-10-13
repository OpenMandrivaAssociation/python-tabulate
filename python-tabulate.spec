Name:		python-tabulate
Version:	0.10.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/t/tabulate/tabulate-%{version}.tar.gz
Summary:	Pretty-print tabular data
URL:		https://pypi.org/project/tabulate/
License:	MIT
Group:		Development/Python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildSystem:	python
BuildArch:	noarch

%description
Pretty-print tabular data

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%{_bindir}/tabulate
%{py_sitedir}/tabulate
%{py_sitedir}/tabulate-%{version}.dist-info
