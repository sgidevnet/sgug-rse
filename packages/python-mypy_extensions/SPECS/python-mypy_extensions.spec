%global srcname mypy_extensions

Name:           python-%{srcname}
Version:        0.4.1
Release:        2%{?dist}
Summary:        Extensions for mypy (separated out from mypy/extensions)

License:        MIT
URL:            https://github.com/python/mypy_extensions
Source:         %{pypi_source}

BuildArch:      noarch

%global _description \
The "mypy_extensions" module defines experimental extensions to the standard\
"typing" module that are supported by the mypy typechecker.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info/

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Initial package
