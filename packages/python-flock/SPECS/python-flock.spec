Name:           python-flock
Version:        0.1
Release:        21%{?dist}
Summary:        Flock object for with statement

License:        BSD
URL:            https://github.com/misli/python-flock
Source:         http://github.srcurl.net/misli/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Flock object uses fcntl.flock to lock (resp. unlock)
file descriptor (fd) with operation (op)
when entering (resp. leaving) runtime context related to it.


%package     -n python3-flock
Summary:        Flock object for with statement

%description -n python3-flock
Flock object uses fcntl.flock to lock (resp. unlock)
file descriptor (fd) with operation (op)
when entering (resp. leaving) runtime context related to it.


%prep
%autosetup


%build
%{py3_build}


%install
%{py3_install}


%files -n python3-flock
%doc README.md LICENSE
%{python3_sitelib}/flock.py
%{python3_sitelib}/__pycache__/flock.*
%{python3_sitelib}/flock-%{version}-py3.*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1-18
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1-15
- Subpackage python2-flock has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Feb 23 2016 Jakub Dorňák <jdornak@redhat.com> - 0.1-7
- add python2- subpackage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Feb 27 2014 Jakub Dorňák <jdornak@redhat.com> - 0.1-1
- new package
