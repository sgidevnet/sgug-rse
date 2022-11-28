Name:           symmetrica
Version:        2.0
Release:        23%{?dist}
Summary:        A Collection of Routines for Solving Symmetric Groups
# Note: they claim it's 'public domain' but then provide this:
# http://www.algorithm.uni-bayreuth.de/en/research/SYMMETRICA/copyright_engl.html
License:        MIT
URL:            http://www.algorithm.uni-bayreuth.de/en/research/SYMMETRICA/
Source0:        http://www.algorithm.uni-bayreuth.de/en/research/SYMMETRICA/SYM2_0_tar.gz
# Sent upstream 8 May 2012.  Sagemath patch to fix namespace collisions on the
# names "sort" and "sum".
Patch0:		symmetrica-sort_sum_rename.patch
# Sent upstream 8 May 2012.  The INT type should always be a 4-byte type, but
# the sources use an incorrect and outdated method of ensuring this.
Patch1:         symmetrica-int.patch
# Will not be sent upstream, as it is GCC-specific.  Add function attributes
# to quiet GCC warnings and improve opportunities for optimization.
Patch2:         symmetrica-attribute.patch
# Patch from sagemath to fix use-after-free in the bruch code.
Patch3:         symmetrica-bruch.patch
# Patch from sagemath to fix issues on 64-bit systems
Patch4:         symmetrica-int32.patch
# Patch from sagemath to fix return values of rec01()
Patch5:         symmetrica-rec01.patch
# Silence -Wsequence-point output from gcc
Patch6:         symmetrica-seq-point.patch
# Add an omitted pointer dereference
Patch7:         symmetrica-deref.patch

BuildRequires:  gcc-c++


%description
Symmetrica is a collection of routines, written in the programming
language C, through which the user can readily write his/her own
programs. Routines which manipulate many types of mathematical objects
are available.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel = %{version}-%{release}


%description    static
The %{name}-static package contains static libraries for
developing applications that use %{name}.


%prep
%autosetup -p0 -c

# Don't print the banner on every library load and API function call
sed -i "s/^\(INT no_banner = \)FALSE/\1TRUE/" de.c

%build
# All the silly *TRUE defines:
#DFLAGS=$(for def in $(grep '#ifdef' *.c | cut -d':' -f2 | cut -d' ' -f2 | egrep .*TRUE | sort | uniq); do echo -D${def}; done)
DFLAGS="-DBINTREETRUE -DBRUCHTRUE -DCHARTRUE -DCYCLOTRUE -DDGTRUE \
  -DELMSYMTRUE -DFFTRUE -DGRALTRUE -DGRAPHTRUE -DGRTRUE -DHOMSYMTRUE \
  -DINTEGERTRUE -DKOSTKATRUE -DKRANZTRUE -DLAURENTTRUE -DLISTTRUE \
  -DLONGINTTRUE -DMATRIXTRUE -DMONOMIALTRUE -DMONOMTRUE \
  -DMONOPOLYTRUE -DNUMBERTRUE -DPARTTRUE -DPERMTRUE -DPLETTRUE \
  -DPOLYTRUE -DPOWSYMTRUE -DREIHETRUE -DSABTRUE -DSCHUBERTTRUE \
  -DSCHURTRUE -DSHUFFLETRUE -DSKEWPARTTRUE -DSQRADTRUE -DTABLEAUXTRUE \
  -DVECTORTRUE -DWORDTRUE -DZYKTRUE"

for file in *.c; do
  if [ $file != "test.c" ] ; then
    gcc %{optflags} -c ${file} -I. -DFAST ${DFLAGS}
  fi
done
ar rcs lib%{name}.a *.o
rm -f *.o
for file in *.c; do
  if [ $file != "test.c" ] ; then
    gcc %{optflags} -fPIC -c ${file} -I. -DFAST ${DFLAGS}
  fi
done
gcc %{optflags} $RPM_LD_FLAGS -shared -Xlinker -hlib%{name}.so.0 \
    -o lib%{name}.so.0.0.0 *.o


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -m 644 lib%{name}.a $RPM_BUILD_ROOT%{_libdir}/
install -m 755 lib%{name}.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/
ln -s lib%{name}.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.0
ln -s lib%{name}.so.0 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
install -m 644 *.h $RPM_BUILD_ROOT%{_includedir}/%{name}/


%ldconfig_scriptlets


%files
%doc *.doc
%{_libdir}/lib%{name}.so.0.0.0
%{_libdir}/lib%{name}.so.0


%files devel
%doc test.c
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so


%files static
%{_libdir}/lib%{name}.a


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Jerry James <loganjerry@gmail.com> - 2.0-21
- Add -bruch patch to fix use-after-free problems in the bruch code
- Add -int32 patch to fix problems on 64-bit systems
- Add -rec01 patch to fix return values of rec01()
- Add -seq-point patch to fix undefined behavior
- Add -deref patch to fix a pointer to character comparison

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0-8
- Do not generate calls to undefined "local" functions.

* Tue May 8 2012 Jerry James <loganjerry@gmail.com> - 2.0-7
- Add patches to fix sagemath build problems, forwarded by pcpa
  <paulo.cesar.pereira.de.andrade@gmail.com>
- Drop unnecessary spec file elements (BuildRoot, clean script, etc.)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Conrad Meyer <konrad@tylerc.org> - 2.0-2
- Generate shared library as well as static library.

* Wed Oct 15 2008 Conrad Meyer <konrad@tylerc.org> - 2.0-1
- Initial package.
