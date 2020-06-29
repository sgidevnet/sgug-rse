%global upname mistune

%global common_description %{expand:
The fastest markdown parser in pure Python, inspired by marked.}

Name:           python-mistune
Version:        0.8.3
Release:        12%{?dist}
Summary:        Markdown parser for Python 

License:        BSD
URL:            https://github.com/lepture/mistune
Source0:        https://github.com/lepture/mistune/archive/v%{version}.tar.gz

BuildRequires:  gcc

BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools

%description %{common_description}


%package -n python3-%{upname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{upname}}

%description -n python3-%{upname} %{common_description}


%prep
%setup -q -n %{upname}-%{version}


%build
%py3_build


%install
%py3_install

pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitearch}
%{_fixperms} %{buildroot}/*


%check
%{__python3} setup.py test


%files -n python3-%{upname}
%doc README.rst
%license LICENSE
%{python3_sitearch}/%{upname}.*
%{python3_sitearch}/%{upname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/__pycache__/%{upname}*


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-10
- Subpackage python2-mistune has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Sep 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-9
- Modernize packaging, drop build dependency on python2-Cython

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Dec 19 2017 Christian Dersch <lupinix@fedoraproject.org> - 0.8.3-1
- new version (0.8.3)
- fixes CVE-2017-15612 and CVE-2017-16876

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.3-7
- Python 2 binary package renamed to python2-mistune
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Christian Dersch <lupinix@mailbox.org> - 0.7.3-1
- new version

* Sat Feb 27 2016 Christian Dersch <lupinix@mailbox.org> - 0.7.2-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 23 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.7.1-1
- new version

* Wed Jun 17 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.6-1
- new upstream release

* Mon Apr 20 2015 Christian Dersch <lupinix@fedoraproject.org> - 0.5.1-1
- new upstream release (0.5.1)

* Fri Dec  5 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.5-1
- new upstream release
- enabled tests

* Thu Dec  4 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.4.1-2
- spec fixes

* Thu Dec  4 2014 Christian Dersch <lupinix@fedoraproject.org> - 0.4.1-1
- initial spec  
