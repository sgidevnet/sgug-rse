%global pypi_name cxxfilt

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Python interface to c++filt/abi::__cxa_demangle

License:        BSD
URL:            https://github.com/afg984/python-cxxfilt
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Demangling C++ symbols in Python and interface to abi::__cxa_demangle.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
Demangling C++ symbols in Python and interface to abi::__cxa_demangle.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
# https://github.com/afq984/python-cxxfilt/issues/4
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.9

* Wed Mar 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Initial package for Fedora
