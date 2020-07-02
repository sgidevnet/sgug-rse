%global pypi_name itanium_demangler

Name:           python-%{pypi_name}
Version:        1.0
Release:        2%{?dist}
Summary:        Pure Python parser for mangled itanium symbols

License:        BSD
URL:            https://github.com/whitequark/python-itanium_demangler
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/whitequark/python-itanium_demangler/master/LICENSE-0BSD.txt
BuildArch:      noarch

%description
The Python Itanium Demangler is a pure Python parser for the Itanium C++ ABI 
symbol mangling language. This demangler generates an abstract syntax tree
from mangled symbols, which can be used for directly extracting type
information, as opposed to having to interpret the C++ source code.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The Python Itanium Demangler is a pure Python parser for the Itanium C++ ABI 
symbol mangling language. This demangler generates an abstract syntax tree
from mangled symbols, which can be used for directly extracting type
information, as opposed to having to interpret the C++ source code.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp -a %{SOURCE1} LICENSE-0BSD.txt

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE-0BSD.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0-1
- Initial package for Fedora
