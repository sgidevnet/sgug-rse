%global svn_release 475

Name:           libreplaygain
Version:        0
Release:        0.13.20110810svn%{svn_release}%{?dist}
Summary:        Gain analysis library from Musepack

License:        LGPLv2+
URL:            http://www.musepack.net/index.php
Source0:        http://files.musepack.net/source/%{name}_r%{svn_release}.tar.gz

BuildRequires:  cmake gcc

%description
Gain analysis library used by Musepack utilities and libraries


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}_r%{svn_release}

# Correct permissions and end of line
chmod 0644 include/replaygain/*.h src/gain_analysis.c
sed -ibackup 's/\r$//' include/replaygain/*.h src/gain_analysis.c

# Don't let it override the compiler flags
# Don't make the build quiet
sed '5,9d' -ibackup CMakeLists.txt


%build
%cmake .
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# Remove static lib
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}.a

mkdir -p $RPM_BUILD_ROOT/%{_includedir}/replaygain/
cp -v include/replaygain/*.h $RPM_BUILD_ROOT/%{_includedir}/replaygain/

%ldconfig_scriptlets


%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/replaygain
%{_libdir}/*.so


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.10.20110810svn
- Add gcc to BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 19 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.1.20110810svn475
- Update as per review: #1018541
- Update version
- Remove unrequired portions
- File inclusions
- Initial rpmbuild

