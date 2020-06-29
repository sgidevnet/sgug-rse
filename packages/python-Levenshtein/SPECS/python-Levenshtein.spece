%global srcname Levenshtein

Name:         python-Levenshtein
Summary:      Python extension computing string distances and similarities
Version:      0.12.0
Release:      15%{?dist}

License:      GPLv2+

# The original site: http://trific.ath.cx/python/levenshtein/
# no longer exists so pointing to the pypi listing instead.
URL:          http://pypi.python.org/pypi/%{name}/

Source:       https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc

BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Levenshtein computes Levenshtein distances, similarity ratios, generalized
medians and set medians of Strings and Unicodes.  Because it's implemented
in C, it's much faster than corresponding Python library functions and
methods.

%package -n python3-%{srcname}
Summary:  %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Levenshtein computes Levenshtein distances, similarity ratios, generalized
medians and set medians of Strings and Unicodes.  Because it's implemented
in C, it's much faster than corresponding Python 3 library functions and
methods.

%prep
%setup -qn %{name}-%{version}

%build
%py3_build
 
%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst NEWS
%license COPYING
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/python_%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-12
- Subpackage python2-Levenshtein has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Rebuild for Python 3.6

* Tue Sep 20 2016 Dominika Krejci <dkrejci@redhat.com> - 0.12.0-1
- Update to 0.12.0
- Add Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-23
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10.1-19
- replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.10.1-12
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Feb 19 2010 Dwayne Bailey <dwayne@translate.org.za> - 0.10.1-11
- Proper fix to source URL

* Thu Feb 18 2010 Dwayne Bailey <dwayne@translate.org.za> - 0.10.1-10
- Use python2-devel in BuildRequires
- Updated source URL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10.1-7
- Rebuild for Python 2.6

* Tue Oct 21 2008 Dwayne Bailey <dwayne@translate.org.za> - 0.10.1-6
- Comments about location of source files
- Update genextdoc.py to v1.5

* Thu Mar 27 2008 Dwayne Bailey <dwayne@translate.org.za> - 0.10.1-5
- Build and package *egg-info
- Fix some rpmlint issues

* Thu Feb 14 2008 Dwayne Bailey <dwayne@translate.org.za> - 0.10.1-4
- Add genextdoc.py as Source not Patch

* Wed Jan 30 2008 Dwayne Bailey <dwayne@translate.org.za> - 0.10.1-3
- Some rpmlint fixes
- Fix document generation

* Wed Jan 23 2008 Dwayne Bailey <dwayne@translate.org.za> - 0.10.1-2
- Add missing genextdoc.py to generate usage documentation

* Wed Jan 23 2008 Dwayne Bailey <dwayne@translate.org.za> - 0.10.1-1
- Initial packaging
