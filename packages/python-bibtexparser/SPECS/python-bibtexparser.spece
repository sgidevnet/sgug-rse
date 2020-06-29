%global srcname bibtexparser

Name:           python-%{srcname}
Version:        1.1.0
Release:        3%{?dist}
Summary:        A BibTeX parsing library

License:        BSD or LGPLv3
URL:            https://github.com/sciunto-org/python-%{srcname}
Source0:        https://github.com/sciunto-org/python-%{srcname}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/sciunto-org/python-bibtexparser/pull/255
Patch0:         python-bibtexparser-1.1.0-shebang-fix.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pyparsing
BuildRequires:  python3-future
BuildRequires:  python3-sphinx

%description
BibtexParser is a python library to parse BibTeX files. The code relies
on pyparsing and is tested with unit tests.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
BibtexParser is a python library to parse BibTeX files. The code relies
on pyparsing and is tested with unittests.

%package doc
Summary: python-bibtexparser documentation

%description doc
Documentation for python-bibtexparser.

%prep
%autosetup -n python-%{srcname}-%{version} -p1

%build
%py3_build
# Generate html documentation.
PYTHONPATH=${PWD} sphinx-build docs/source html
# Remove the sphinx-build leftovers.
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{srcname}
%doc CHANGELOG CONTRIBUTORS.txt README.rst requirements.txt
%license COPYING
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/bibtexparser/

%files doc
%doc html
%license COPYING

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.9

* Wed Mar 25 2020 W. Michael Petullo <mike@flyn.org> - 1.1.0-2
- Patch out shebang lines from non-executable Python files
- License is BSD or LGPLv3
- Update Source0
- Generate documentation using Sphinx

* Thu Mar 12 2020 W. Michael Petullo <mike@flyn.org> - 1.1.0-1
- Initial package
