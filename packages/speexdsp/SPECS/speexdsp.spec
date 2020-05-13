Name:           speexdsp
Version:        1.2
%global rc_ver  rc3
Release:        0.16.%{rc_ver}%{?dist}
Summary:        A voice compression format (DSP)

License:        BSD
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/%{name}-%{version}%{rc_ver}.tar.gz
# a patch to speex (774c87d) was done usptream to fix this issue but it seems it
# hasn't been replicated in speexdsp. Issue seen in at least pjproject
# upstream ML thread http://lists.xiph.org/pipermail/speex-dev/2014-May/008488.html
Patch0:         speexdsp-fixbuilds-774c87d.patch

BuildRequires: libtool autoconf automake
# speexdsp was split from speex in 1.2rc2. As speexdsp does not depend on
# speex, a versioned conflict is required.
Conflicts: speex <= 1.2-0.21.rc1

%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the DSP package, see the speex package for the codec part.

%package devel
Summary: 	Development package for %{name}
Requires: 	%{name}%{?_isa} = %{version}-%{release}
# speexdsp was split from speex in 1.2rc2. As speexdsp does not depend on
# speex, a versioned conflict is required.
Conflicts: speex-devel <= 1.2-0.21.rc1

%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{name}

This is the DSP package, see the speex package for the codec part.


%prep
%setup -q -n %{name}-%{version}%{rc_ver}
%patch0 -p1 -b .inc

%build
autoreconf -vif
%configure \
%ifarch aarch64
	--disable-neon \
%endif
	--disable-static

make %{?_smp_mflags} V=1

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install

# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

#%%ldconfig_scriptlets


%files
%doc AUTHORS COPYING TODO ChangeLog README NEWS doc/manual.pdf
%doc %{_docdir}/speexdsp/manual.pdf
%{_libdir}/libspeexdsp.so.*

%files devel
%{_includedir}/speex
%{_libdir}/pkgconfig/speexdsp.pc
%{_libdir}/libspeexdsp.so

%changelog
* Wed May 13 2020  Alexander Tafarte <notes2@gmx.de> - 1.2-0.17.rc3
- compiles on Irix 6.5 with sgug-rse gcc 9.2 , no tests available.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.16.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.15.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.14.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.13.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.12.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.11.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.10.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.9.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Jared Smith <jsmith@fedoraproject.org> - 1.2-0.8.rc3
- Fix building on EPEL6/EPEL7 again, due to manual.pdf

* Fri Oct 23 2015 Jared Smith <jsmith@fedoraproject.org> - 1.2-0.7.rc3
- Fix building by making sure the manual.pdf file is included in the docs

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.6.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0.5.rc3
- Add patch similar to what was already done upstream in speex but not dsp

* Thu Jan 15 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0.4.rc3
- Fix build on aarch64 (disable NEON)

* Mon Jan 05 2015 David King <amigadave@amigadave.com> - 1.2.0.3.rc3
- Update to 1.2rc3

* Sun Dec 14 2014 David King <amigadave@amigadave.com> - 1.2-0.2.rc2.20141214git
- Use a git snapshot, to ensure that speex_buffer.h is present

* Fri Dec 12 2014 David King <amigadave@amigadave.com> - 1.2-0.1.rc2
- New package, split from speex (#1172829)
