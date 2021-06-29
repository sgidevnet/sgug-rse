Name:           klt
Version:        1.3.4
Release:        20%{?dist}
Summary:        An implementation of the Kanade-Lucas-Tomasi feature tracker

License:        Public Domain
URL:            http://www.ces.clemson.edu/~stb/%{name}/index.html
Source0:        http://www.ces.clemson.edu/~stb/%{name}/%{name}%{version}.zip

# https://bugzilla.redhat.com/show_bug.cgi?id=1037150
Patch0:         0001-format-security.patch
BuildRequires:  gcc

%description

KLT is an implementation, in the C programming language, of a 
feature tracker for the computer vision community.  The source 
code is in the public domain, available for both commercial and 
non-commercial use.

The tracker is based on the early work of Lucas and Kanade, 
was developed fully by Tomasi and Kanade, and was explained clearly 
in the paper by Shi and Tomasi. Later, Tomasi proposed a slight 
modification which makes the computation symmetric with respect 
to the two images -- the resulting equation is derived in the 
unpublished note by myself.  Briefly, good features are located 
by examining the minimum eigenvalue of each 2 by 2 gradient 
matrix, and features are tracked using a Newton-Raphson method of 
minimizing the difference between the two windows. Multi-resolution 
tracking allows for relatively large displacements between images. 
The affine computation that evaluates the consistency of features 
between non-consecutive frames was implemented by Thorsten 
Thormaehlen several years after the original code and documentation 
were written.

%package devel
Requires: %{name} = %{version}-%{release}
Summary:  This package contains development files for %{name}

%description devel
This package provides headers and shared libraries for %{name}

%package static
Requires: %{name} = %{version}-%{release}
Summary:  This package contains static libraries for %{name}

%description static
This package contains the static libraries 
provided by %{name}. 

%package doc
Requires: %{name} = %{version}-%{release}
Summary:  This package contains documentation for %{name}

%description doc
This package contains documentation files for %{name}

%prep
%setup -q -n %{name}
sed -i 's/\r//' README.txt 
sed -i 's/\r//' speed.txt
sed -i 's/\r//' example?.c
sed -i '/FLAG1/d' Makefile
sed -i '/rm -f \*\.o/d' Makefile

%patch0


%build
%global klt_version %{version}
%global klt_version_major 1

export CFLAGS="$RPM_OPT_FLAGS -fPIC"

make lib %{?_smp_mflags} 
gcc -shared -Wl,-soname,libklt.so.%{klt_version_major} \
    -o libklt.so.%{klt_version} convolve.o error.o pnmio.o pyramid.o selectGoodFeatures.o \
    storeFeatures.o trackFeatures.o klt.o klt_util.o writeFeatures.o 

ln -sf libklt.so.%{klt_version} libklt.so.%{klt_version_major}
ln -sf libklt.so.%{klt_version} libklt.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

for f in *.so* *.a ; do
    cp -a $f $RPM_BUILD_ROOT/%{_libdir}/$f
done

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-doc
cp -av doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-doc/

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-doc/examples/
install -m 0644 -p example?.c -t $RPM_BUILD_ROOT%{_docdir}/%{name}-doc/examples/
install -m 0644 -p *.pgm -t $RPM_BUILD_ROOT%{_docdir}/%{name}-doc/examples/

install -d $RPM_BUILD_ROOT%{_includedir}/%{name}
install -m 0644 -p *.h -t $RPM_BUILD_ROOT%{_includedir}/%{name}

%files
%doc README.txt speed.txt
%{_libdir}/libklt.so.%{klt_version}
%{_libdir}/libklt.so.%{klt_version_major}

%files devel
%{_libdir}/libklt.so
%{_includedir}/%{name}/

%files static
%{_libdir}/*.a

%files doc
%{_docdir}/%{name}-doc


%ldconfig_scriptlets


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.4-17
- Add gcc to BRs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 05 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.3.4-8
- Patch for format-security
- https://bugzilla.redhat.com/show_bug.cgi?id=1037150

* Wed Dec 04 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.3.4-7
- Fix docs
- https://bugzilla.redhat.com/show_bug.cgi?id=1001274

* Fri Oct 11 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.3.4-6
- https://bugzilla.redhat.com/show_bug.cgi?id=1001274

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 06 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.4-2
- spec bump for gcc 4.7 rebuild

* Mon Jun 27 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.4-1
- create shared objects also
- create a separate subpackage for static libs

* Thu Jun 16 2011 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.3.4-1
- Remove debug package, look at header comment for comment
- Honour optflags
- Initial rpm build
