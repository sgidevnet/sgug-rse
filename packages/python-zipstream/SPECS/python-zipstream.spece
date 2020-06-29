%global srcname zipstream
%global desc zipstream.py is a zip archive generator based on python 3.3's zipfile.py.\
It was created to generate a zip file generator for streaming (ie web apps).

Name:           python-%{srcname}
Version:        1.1.4
Release:        19%{?dist}
Summary:        ZIP archive generator for Python

License:        GPLv3+
URL:            https://github.com/allanlei/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch


%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-nose

%description -n python3-%{srcname}
%{desc}
Python 3 version.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test



%files -n python3-%{srcname}
%license LICENSE
%doc README.* 
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.1.4-17
- Rebuilt for un-retire

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.4-12
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 07 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.4-4
- Move BR into the sub pkg
- Fix prep section 

* Thu Jul 07 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.4-3
- Use more macros
- Fix BR
- Simplify testsuite invocation

* Thu Jul 07 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.4-2
- Fix typos
- Enable check section

* Tue Jul 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.4-1
- Initial spec 
