%global srcname empy
%global sum A powerful and robust template system for Python

Name:           python-empy
Version:        3.3.4
Release:        7%{?dist}
Summary:        %{sum}
License:        LGPLv2+
URL:            http://www.alcyone.com/software/empy/
Source:         http://www.alcyone.com/software/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
EmPy is a system for embedding Python expressions and statements in template
text; it takes an EmPy source file, processes it, and produces output. 

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
EmPy is a system for embedding Python expressions and statements in template
text; it takes an EmPy source file, processes it, and produces output. 

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license COPYING
%doc README version.txt
%{python3_sitelib}/__pycache__/em.*.pyc
%{python3_sitelib}/em.py
%{python3_sitelib}/empy-*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 24 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-5
- Subpackage python2-empy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 2019 Filipe Rosset <rosset.filipe@gmail.com> - 3.3.4-1
- Update to latest 3.3.4 upstream release, fixes rhbz #1697143

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.3-3
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Filipe Rosset <rosset.filipe@gmail.com> - 3.3.3-2
- Bump to 3.3.3 and fix packaging issues

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.3.2-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.3.2-11
- Rebuild for Python 3.6

* Sun Dec 04 2016 Filipe Rosset <rosset.filipe@gmail.com> - 3.3.2-10
- rebuilt to fix rhbz #1388272 (use latest python packaging guidelines)

* Sat Nov 05 2016 Filipe Rosset <rosset.filipe@gmail.com> - 3.3.2-9
- Spec clean up

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Mar 08 2014 Filipe Rosset <rosset.filipe@gmail.com> - 3.3.2-2
- Fix packaging issues, spec cleanup
- Now compatible with python2 and python3 rhbz #1073768 

* Fri Mar 07 2014 Filipe Rosset <rosset.filipe@gmail.com> - 3.3.2-1
- Update to 3.3.2

* Fri Jan 24 2014 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-1
- Update to 3.3.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
