%global pname tempdir

%global desc \
Having to manually manage temporary directories is annoying. \
So this class encapsulates temporary directories which just disappear after \
use, including contained directories and files. \
Temporary directories are created with tempfile.mkdtemp and thus safe from \
race conditions. Cleanup might not work on windows if files are still opened. \


Name: python-%{pname}
Version: 0.7.1
Release: 15%{?dist}
Summary: Automatically manage temporary directories, based on tempfile.mkdtemp
License: MIT
URL: https://bitbucket.org/another_thomas/tempdir
Source0: https://pypi.python.org/packages/source/t/%{pname}/%{pname}-%{version}.tar.gz
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-devel
%{?python_provide:%python_provide python3-%{pname}}

%description -n python3-%{pname}
%{desc}

%prep
%setup -q -n %{pname}-%{version}
rm -r tempdir.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pname}
%license docs/license.rst
%doc docs/use.rst
%{python3_sitelib}/%{pname}-%{version}-py3.?.egg-info
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/tempdir.py

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-9
- Subpackage python2-tempdir has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Mar 11 2016 Dominik Mierzejewski <dominik@greysector.net> 0.7.1-1
- update to 0.7.1
- remove pre-built egg-info

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Dominik Mierzejewski <dominik@greysector.net> 0.6-1
- initial build
