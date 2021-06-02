Name:          bcg729
Version:       1.0.4
Release:       5%{?dist}
Summary:       Opensource implementation of the G.729 codec

License:       GPLv2+
URL:           https://github.com/BelledonneCommunications/bcg729
Source0:       https://github.com/BelledonneCommunications/bcg729/archive/%{version}/%{name}-%{version}.tar.gz
# Test data is not redistributible
# Source1:       http://www.belledonne-communications.com/downloads/bcg729-patterns.zip

BuildRequires: automake autoconf libtool
BuildRequires: gcc


%description
bcg729 is an opensource implementation of both encoder and decoder of the
ITU G729 Annex A speech codec.
The library written in C 99 is fully portable and can be executed on many
platforms including both ARM  processor and x86.
bcg729 supports concurrent channels encoding/decoding for multi call
application such conferencing.


%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
Development files for %{name}.


%prep
%autosetup -p1
# unzip -qq -d test %%{SOURCE1}


%build
./autogen.sh
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot}%{_libdir} -type f -name '*.la' -delete -print

%check
# Test data is not redistributible
# make check


%ldconfig_scriptlets


%files
%doc AUTHORS README.md
%license COPYING
%{_libdir}/lib%{name}.so.*


%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Sandro Mani <manisandro@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Sat Mar 18 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 28 2017 Sandro Mani <manisandro@gmail.com> - 1.0.3-1
- Update to 1.0.3

* Fri Jan 06 2017 Sandro Mani <manisandro@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Thu Jul 28 2016 Sandro Mani <manisandro@gmail.com> - 1.0.1-2
- Remove OpenSSL BRs

* Thu Jul 28 2016 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Thu Jul 28 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.0.0-3
- add test data, build (but don't install) static library and enable tests

* Wed Jul 20 2016 Sandro Mani <manisandro@gmail.com> - 1.0.0-2
- Move autoreconf to build
- BR: pkgconfig(ortp)
- License is GPLv2+
- Change command to delete *.la files
- Use %%name in %%files
- Don't fix FSF addresses

* Wed Jul 20 2016 Sandro Mani <manisandro@gmail.com> - 1.0.0-1
- Initial package
