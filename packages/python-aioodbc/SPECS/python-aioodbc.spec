%global srcname aioodbc

Name:           python-%{srcname}
Version:        0.3.3
Release:        5%{?dist}
Summary:        Library for accessing a ODBC databases from the asyncio

License:        ASL 2.0
URL:            https://github.com/aio-libs/aioodbc
Source:         %{pypi_source}

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname}
%{summary}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc CHANGES.txt README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-2
- Rebuilt for Python 3.8

* Sat Aug 03 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.7

* Sun Mar 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.3-1
- Initial package
