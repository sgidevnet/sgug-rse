%global srcname mypy_extensions

Name:           python-%{srcname}
Version:        0.4.3
Release:        3%{?dist}
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

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.3-1
- Update to 0.4.3

* Sun Dec 29 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 0.4.1-5
- Fix output package name

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Initial package
