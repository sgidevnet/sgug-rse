%global pypi_name cchardet

# nose dependency for the unit tests
# https://github.com/PyYoshi/cChardet/issues/63
Name:           python-%{pypi_name}
Version:        2.1.6
Release:        3%{?dist}
Summary:        High speed universal character encoding detector

License:        MPLv1.1 or GPLv2 or LGPLv2
URL:            https://github.com/PyYoshi/cChardet
Source0:        %{pypi_source}

BuildRequires:  gcc-c++
# https://github.com/PyYoshi/cChardet/issues/62
#BuildRequires:  uchardet-devel

Provides:       bundle(uchardet)

%description
cChardet is high speed universal character encoding detector.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
cChardet is high speed universal character encoding detector.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove bundled uchardet
#rm -rf src/ext

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst src/ext/uchardet/README.md src/ext/uchardet/doc/README.maintainer
%license COPYING
%{_bindir}/cchardetect
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.6-3
- Rebuilt for Python 3.9

* Sun May 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.6-2
- Add comment about nose
- Update license tag (rhbz#1834977)

* Tue May 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.6-1
- Initial package for Fedora
