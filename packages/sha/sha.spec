Name:		sha
#Upstream will continue in the next version 
#with the behavior of shared libraries (specifically version 1.2)
Version:	1.0.4b
Release:	15%{?dist}
Summary:	File hashing utility
License:	BSD
URL:		http://hg.saddi.com/sha-asaddi
Source0:	http://www.saddi.com/software/%{name}/dist/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:	pkgconfig

%description
file hashing utility that uses the
SHA-1, SHA-256, SHA-384, & SHA-512 hash algorithms.
It can be used for file integrity checking, 
remote file comparisons, etc. 
The portable algorithm implementations 
can be useful in other projects too

%package devel
Summary:	Development files for sha
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the libraries needed to develop applications
that use sha

%prep
%setup -q

%build
%configure \
	--disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install
rm -f %{buildroot}/%{_libdir}/*.la
mkdir -p %{buildroot}/%{_includedir}/sha
install -pm 644 *.h %{buildroot}/%{_includedir}/sha

%ldconfig_scriptlets
%ldconfig_scriptlets -n sha-devel

%files
%doc LICENSE README README.SHA ChangeLog
%{_bindir}/sha
%{_mandir}/man1/sha.1*
%{_libdir}/*.so.*

%files devel
%doc LICENSE README.SHA
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*.h
%{_libdir}/*.so

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 1.0.4b-2
- Moved headers files in devel package to subdirectory in /usr/include based
  on https://fedoraproject.org/wiki/Packaging:Conflicts#Header_Name_Conflicts 

* Sun Oct 28 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 1.0.4b-1
- Update to version 1.0.4b includes separate license, provided by upstream
- Remove macro clean

* Mon Oct 22 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 1.0.4a-4
- Fix incorrect ownership of manpages

* Thu Oct 04 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 1.0.4a-3
- Add comment of the Upstream about next release with the bahaviour of shared 
  libraries

* Wed Sep 26 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 1.0.4a-2
- Changes to match the correct architecture in the section Requires of
  devel package
- Remove versioned libraries to the base package
- Remove the c files to section doc of the devel package
- Add README.SHA to section doc of the devel package

* Sun Sep 23 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 1.0.4a-1
- Initial packaging
