Name:           alglib
Version:        3.15.0
Release:        2%{?dist}
Summary:        A numerical analysis and data processing library

License:        GPLv2+
URL:            http://www.alglib.net/
Source0:        http://www.alglib.net/translator/re/%{name}-%{version}.cpp.gpl.tgz
Source1:        CMakeLists.txt
# Extracted from manual.cpp.html
Source2:        bsd.txt

# Make test output more verbose
Patch0:         alglib_verbose-tests.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
ALGLIB is a cross-platform numerical analysis and data processing library.
ALGLIB features include:
 - Data analysis (classification/regression, including neural networks)
 - Optimization and nonlinear solvers
 - Interpolation and linear/nonlinear least-squares fitting
 - Linear algebra (direct algorithms, EVD/SVD), direct and iterative linear
   solvers, Fast Fourier Transform and many other algorithms (numerical
   integration, ODEs, statistics, special functions)



%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
License:        BSD
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the %{name} API documentation.


%prep
%autosetup -p1 -n cpp
cp %{SOURCE1} .
cp %{SOURCE2} .

# Fix permissions and line endings
chmod 644 gpl2.txt
chmod 644 manual.cpp.html
sed -i 's|\r||g' manual.cpp.html


%build
mkdir build
(
cd build
# disable FMA support to get it pass all tests
%ifarch aarch64 %{power64} s390 s390x
export CXXFLAGS="$RPM_OPT_FLAGS -ffp-contract=off"
export CFLAGS="$RPM_OPT_FLAGS -ffp-contract=off"
%endif
%cmake -DALGLIB_VERSION=%{version} ..
%make_build
)


%install
%make_install -C build
ln -s libalglib-%{version}.so %{buildroot}%{_libdir}/libalglib.so


%check
pushd build
LD_LIBRARY_PATH=$PWD ./test_c || false
LD_LIBRARY_PATH=$PWD ./test_i || false
popd


%ldconfig_scriptlets


%files
%license gpl2.txt
%{_libdir}/libalglib-%{version}.so

%files devel
%{_includedir}/%{name}/
%{_libdir}/libalglib.so

%files doc
%license bsd.txt
%doc manual.cpp.html


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Sandro Mani <manisandro@gmail.com> - 3.15.0-1
- Update to 3.15.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Sandro Mani <manisandro@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 3.13.0-3
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 29 2017 Sandro Mani <manisandro@gmail.com> - 3.13.0-1
- Update to 3.13.0

* Wed Aug 23 2017 Sandro Mani <manisandro@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Sandro Mani <manisandro@gmail.com> - 3.11.0-1
- Update to 3.11.0

* Tue Mar 14 2017 Sandro Mani <manisandro@gmail.com> - 3.10.0-5
- Make test output more vebose
- Temporarily ignore test failures on i686 due to http://bugs.alglib.net/view.php?id=689

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 3.10.0-2
- disable FMA support to get it pass all tests on secondary architectures

* Sat Aug 22 2015 Sandro Mani <manisandro@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.9.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Dec 13 2014 Sandro Mani <manisandro@gmail.com> - 3.9.0-1
- Update to 3.9.0
- Use version as library name suffix, not as soname

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 9 2014 Jakub Čajka <jcajka@redhat.com> - 3.8.2-5
- Made exlusive for primary archs

* Wed Jun 18 2014 Sandro Mani <manisandro@gmail.com> - 3.8.2-4
- Add missing license tag

* Wed Jun 18 2014 Sandro Mani <manisandro@gmail.com> - 3.8.2-3
- Add bsd.txt to doc subpackage (license text extracted from manual.cpp.html)

* Wed Jun 18 2014 Sandro Mani <manisandro@gmail.com> - 3.8.2-2
- Add doc subpackage with correct license
- Run tests
- Fix unversioned so included in main package
- Fix manual.cpp.html permissions, line endings

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 3.8.2-1
- Initial package
