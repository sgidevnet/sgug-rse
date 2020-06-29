%global srcname cerealizer
%global sum Secure pickle-like module

Name:			python-%{srcname}
Summary: 		%{sum}
Version:		0.8.2
Release:		7%{?dist}
License:		Python
Source0:		https://files.pythonhosted.org/packages/5a/2b/8a2ff505db0ef7ce59f700b96898369b22a823c8d9191eba37639e568667/Cerealizer-%{version}.tar.gz
URL:			http://www.lesfleursdunormal.fr/static/informatique/cerealizer/index_en.html
BuildArch:		noarch
BuildRequires:		python3-devel

%description
Cerealizer is a secure pickle-like module. It support basic types (int, string,
unicode, tuple, list, dict, set,...), old and new-style classes (you need to 
register the class for security), object cycles, and it can be extended to 
support C-defined type.

%package -n python3-%{srcname}
Summary:                %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Cerealizer is a secure pickle-like module. It support basic types (int, string,
unicode, tuple, list, dict, set,...), old and new-style classes (you need to 
register the class for security), object cycles, and it can be extended to 
support C-defined type.

%prep
%setup -q -n Cerealizer-%{version}

%build
/usr/bin/python3 ./setup.py build

%install
/usr/bin/python3 ./setup.py install --skip-build --root $RPM_BUILD_ROOT

%files -n python3-%{srcname}
%doc README.rst PKG-INFO
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct  5 2018 Tom Callaway <spot@fedoraproject.org> - 0.8.2-1
- update to 0.8.2
- drop python2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 0.8-1
- update to 0.8
- enable python3 packaging

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Aug 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7-1
- update to 0.7

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6-4
- Rebuild for Python 2.6

* Sat Apr  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.6-3
- Add egg-info files (fix FTBFS bz 440814)

* Sat Nov 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.6-2
- add check

* Wed Nov 14 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.6-1
- Initial package for Fedora
