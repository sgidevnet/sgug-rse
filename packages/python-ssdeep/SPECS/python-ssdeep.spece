%global pypi_name ssdeep

%global pypi_description A straightforward Python module for ssdeep by Jesse Kornblum, \
which is a library for computing context triggered piecewise hashes (CTPH). \
Also called fuzzy hashes, CTPH can match inputs that have homologies. \
Such inputs have sequences of identical bytes in the same order, although \
bytes in between these sequences may be different in both content and length.


Name: python-%{pypi_name}
Summary: Python wrapper for the ssdeep library
License: LGPLv3+

Version: 3.4
Release: 4%{?dist}

URL: https://github.com/DinoTools/python-ssdeep/
Source0: %pypi_source

BuildRequires: gcc
BuildRequires: ssdeep-devel

BuildRequires: python3-cffi >= 0.8.6
BuildRequires: python3-devel
BuildRequires: python3-pytest-runner
BuildRequires: python3-setuptools
BuildRequires: python3-six >= 1.4.1
BuildRequires: python3-sphinx


%description
%{pypi_description}


%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{pypi_description}


%package -n python3-%{pypi_name}-doc
Summary: Documentation for python3-%{pypi_name}
BuildArch: noarch

%description -n python3-%{pypi_name}-doc
This package contains documentation (in HTML and man page format)
for the ssdeep Python3 module.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build

pushd docs/
make man
make html


%install
%py3_install

install -d -m 755 %{buildroot}%{_mandir}/man5/
install -m 644 docs/build/man/pythonssdeep.1 %{buildroot}%{_mandir}/man5/python3-%{pypi_name}.5


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc CHANGELOG.rst CONTRIBUTING.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-*.egg-info/

%files -n python3-%{pypi_name}-doc
%doc docs/build/html/*
%{_mandir}/man5/python3-%{pypi_name}.5*


%changelog
* Thu Jun 25 2020 Artur Iwicki <fedora@svgames.pl> - 3.4-4
- Add an explicit BuildRequires on python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4-3
- Rebuilt for Python 3.9

* Thu Mar 05 2020 Artur Iwicki <fedora@svgames.pl> - 3.4-2
- Fix package description and BuildRequires
- Add documentation in a -doc package

* Thu Feb 27 2020 Artur Iwicki <fedora@svgames.pl> - 3.4-1
- Initial packaging
