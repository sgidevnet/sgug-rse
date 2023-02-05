Name:    gmm
Summary: A generic C++ template library for sparse, dense and skyline matrices
Version: 5.2
Release: 4%{?dist}

License: LGPLv2+ 
URL:     http://getfem.org/gmm.htm
Source0: http://download-mirror.savannah.gnu.org/releases/getfem/stable/gmm-%{version}.tar.gz

BuildArch: noarch

# for %%check mostly
BuildRequires: gcc-c++
BuildRequires: perl-interpreter

%description
%{summary}.

%package devel
Summary:A generic C++ template library for sparse, dense and skyline matrices
Provides: %{name} = %{version}-%{release}
Provides: gmm++-devel = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q


%build
%configure


%install
%make_install


%check
%make_build check -k || cat tests/test-suite.log ||:


%files devel
#doc README
%license COPYING
%{_includedir}/gmm/


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.2-1
- 5.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 20 2016 Rex Dieter <rdieter@fedoraproject.org> 5.0-1
- gmm-5.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 05 2014 Rex Dieter <rdieter@fedoraproject.org> 4.3-1
- gmm-4.3 (#1135695)

* Tue Jun 24 2014 Rex Dieter <rdieter@fedoraproject.org> 4.2-1
- gmm-4.2, add %%check section

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 30 2010 Steven M. Parrish <smparrish@gmail.com> - 4.0.0-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Steven Parrish <smparrish@shallowcreek.net> 3.1-1
- New upstream release

* Wed May 28 2008 Steven Parrish <smparrish[at]shallowcreek.net> 3.0-3
- corrected license

* Wed May 28 2008 Rex Dieter <rdieter@fedoraproject.org> 3.0-2
- name gmm
- -devel: Provides: gmm++-devel = ...

* Tue May 27 2008 Steven Parrish <smparrish[at]shallowcreek.net> 3.0-1
-  Initial SPEC file

