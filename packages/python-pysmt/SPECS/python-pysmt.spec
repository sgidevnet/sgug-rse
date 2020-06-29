%global pypi_name pysmt

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        3%{?dist}
Summary:        Solver-agnostic library for SMT Formulae manipulation and solving

License:        ASL 2.0
URL:            http://www.pysmt.org
Source0:        https://github.com/pysmt/pysmt/releases/download/v%{version}/PySMT-%{version}.tar.gz
BuildArch:      noarch

%description
A library for SMT formulae manipulation and solving pySMT makes working
with Satisfiability Modulo Theory simple. Among others, you can:

* Define formulae in a solver independent way in a simple and inutitive way
* Write ad-hoc simplifiers and operators
* Dump your problems in the SMT-Lib format
* Solve them using one of the native solvers
* Wrapping any SMT-Lib complaint

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
#BuildRequires:  python3-nose
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
A library for SMT formulae manipulation and solving pySMT makes working
with Satisfiability Modulo Theory simple. Among others, you can:

* Define formulae in a solver independent way in a simple and intuitive way
* Write ad-hoc simplifiers and operators
* Dump your problems in the SMT-Lib format
* Solve them using one of the native solvers
* Wrapping any SMT-Lib complaint

%prep
%autosetup -n PySMT-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' pysmt/{cmd/shell.py,constants.py}

%build
%py3_build

%install
%py3_install

# https://github.com/pysmt/pysmt/issues/608
#%%check
#export NOSE_PROCESSES=4
#export NOSE_PROCESS_TIMEOUT=240
#export PYTHONDONTWRITEBYTECODE=True
#nosetests-%%{python3_version} -v -x

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst docs/*.rst docs/tutorials/
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/PySMT-%{version}-py*.egg-info/
%exclude %{python3_sitelib}/%{pypi_name}/test/
%{_bindir}/pysmt
%{_bindir}/pysmt-install
%{_bindir}/pysmt-shell

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.9

* Thu Mar 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-2
- Fix typo in description (rhbz#1808467)

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Initial package for Fedora
