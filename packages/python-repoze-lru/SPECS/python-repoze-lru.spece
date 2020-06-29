%global modname repoze.lru

Name:           python-repoze-lru
Version:        0.7
Release:        8%{?dist}
Summary:        A tiny LRU cache implementation and decorator

License:        BSD
URL:            http://pypi.python.org/pypi/repoze.lru
Source0:        %pypi_source %{modname}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
repoze.lru is a LRU (least recently used) cache implementation. Keys and values\
that are not used frequently will be evicted from the cache faster than keys\
and values that are used frequently.\


%description %_description

%package -n python3-repoze-lru
Summary:        A tiny LRU cache implementation and decorator
%{?python_provide:%python_provide python3-repoze-lru}

%description -n python3-repoze-lru
repoze.lru is a LRU (least recently used) cache implementation. Keys and values
that are not used frequently will be evicted from the cache faster than keys
and values that are used frequently.


%prep
%setup -q -n %{modname}-%{version}
rm -rf %{modname}.egg-info


%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-repoze-lru
%doc README.rst LICENSE.txt COPYRIGHT.txt CONTRIBUTORS.txt
%{python3_sitelib}/repoze/lru
%{python3_sitelib}/%{modname}-%{version}*

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-5
- Subpackage python2-repoze-lru has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7-1
- Update to 0.7
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-19
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4-18
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 0.7.19-5
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4-15
- Python 2 binary package renamed to python2-repoze-lru
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4-12
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured>fr - 0.4-5
- Change BR from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Ralph Bean <rbean@redhat.com> - 0.4-3
- Removed clean section.
- Removed defattr.
- Removed removing of buildroot in install section.
- Added removal of egg-info in prep section.
- Added python3 subpackage.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 13 2012 Luke Macken <lmacken@redhat.com> - 0.4-1
- Update to 0.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan  2 2010 Luke Macken <lmacken@redhat.com> - 0.3-1
- Initial package
