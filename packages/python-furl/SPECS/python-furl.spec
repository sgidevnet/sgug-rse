%{?python_enable_dependency_generator}

%global modname furl

Name:           python-%{modname}
Version:        1.2
Release:        9%{?dist}
Summary:        URL manipulation made simple

License:        Unlicense
URL:            https://github.com/gruns/furl
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}. This module let you access and modify the components (parts) of a
URL like scheme (http, https), host, port.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.8.0
BuildRequires:  python3-orderedmultidict >= 1.0

%description -n python3-%{modname}
%{summary}. This module let you access and modify the components (parts) of a
URL like scheme (http, https), host, port.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
sed -i -e "s/'flake8', //" setup.py

%build
%py3_build

%install
%py3_install

%check
touch tests/__init__.py
%{__python3} setup.py test

%files -n python3-%{modname}
%license LICENSE.md
%doc API.md README.md changelog.txt
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-3
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-1
- Update to 1.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.7-1
- Update to 0.5.7 (RHBZ #1429064)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.6-2
- Rebuild for Python 3.6

* Mon Oct 24 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.5.6-1
- Update to 0.5.6

* Sat Sep 24 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.5.3-1
- Update to 0.5.3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.93-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 05 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.4.93-1
- Update to 0.4.93

* Sun Apr 03 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.4.92-1
- Initial package
