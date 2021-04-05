Name:           http-parser
Version:        2.9.3
Release:        1%{?dist}
Summary:        HTTP request/response parser for C

License:        MIT
URL:            https://github.com/nodejs/http-parser
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc

%description
This is a parser for HTTP messages written in C. It parses both requests and
responses. The parser is designed to be used in performance HTTP applications.
It does not make any syscalls nor allocations, it does not buffer data, it can
be interrupted at anytime. Depending on your architecture, it only requires
about 40 bytes of data per message stream (in a web server that is per
connection).

%package devel
Summary:        Development headers and libraries for http-parser
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Development headers and libraries for http-parser.

%prep
%autosetup -p1
# TODO: try to send upstream?
cat > meson.build << EOF
project('%{name}', 'c', version : '%{version}')
install_headers('http_parser.h')
foreach x : [['http_parser',        ['-DHTTP_PARSER_STRICT=0']],
             ['http_parser_strict', ['-DHTTP_PARSER_STRICT=1']]]
  lib = library(x.get(0), 'http_parser.c',
                c_args : x.get(1),
                version : '%{version}',
                install : true)
  test('test-@0@'.format(x.get(0)),
       executable('test-@0@'.format(x.get(0)), 'test.c',
                  c_args : x.get(1),
                  link_with : lib),
       timeout : 60)
endforeach
EOF

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

#%%ldconfig_scriptlets

%files
%license LICENSE-MIT
%doc AUTHORS README.md
%{_libdir}/libhttp_parser.so.*
%{_libdir}/libhttp_parser_strict.so.*

%files devel
%{_includedir}/http_parser.h
%{_libdir}/libhttp_parser.so
%{_libdir}/libhttp_parser_strict.so

%changelog
* Tue Mar 23 2021  HAL <notes2@gmx.de> - 2.9.2-3
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.9.2-1
- Update to 2.9.2

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 2.9.1-2
- Rebuild with Meson fix for #1699099

* Thu Apr 11 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.9.1-1
- Update to 2.9.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.8.1-1
- Update to 2.8.1

* Sat Feb 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0
- Switch to meson buildsystem

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.7.1-8
- Switch to %%ldconfig_scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.7.1-4
- Use CMake buildsystem

* Tue Oct 25 2016 Nathaniel McCallum <npmccallum@redhat.com> - 2.7.1-3
- Add (upstreamed) status code patch

* Tue Aug 16 2016 Stephen Gallagher <sgallagh@redhat.com> - 2.7.1-2
- Upgrade to version 2.7.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 01 2015 Stephen Gallagher <sgallagh@redhat.com> 2.6.0-1
- Upgrade to version 2.6.0
- Change to new upstream at https://github.com/nodejs/http-parser/

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9.20121128gitcd01361
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0-8.20121128gitcd01361
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7.20121128gitcd01361
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6.20121128gitcd01361
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5.20121128gitcd01361
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4.20121128gitcd01361
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0-3.20121128gitcd01361
- latest git snapshot
- fixes buffer overflow in tests

* Tue Nov 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0-2.20121110git245f6f0
- latest git snapshot
- fixes tests
- use SMP make flags
- build as Release instead of Debug
- ship new strict variant

* Sat Oct 13 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0-1
- new upstream release 2.0
- migrate to GYP buildsystem

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0-1
- New upstream release 1.0
- Remove patches, no longer needed for nodejs
- Fix typo in -devel description
- use github tarball instead of checkout

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6.20100911git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Lubomir Rintel <lkundrak@v3.sk> - 0.3-5.20100911git
- Add support for methods used by node.js

* Thu Nov  4 2010 Dan HorÃ¡k <dan[at]danny.cz> - 0.3-4.20100911git
- build with -fsigned-char

* Wed Sep 29 2010 jkeating - 0.3-3.20100911git
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.3-2.20100911git
- Call ldconfig (Peter Lemenkov)

* Fri Sep 17 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.3-1.20100911git
- Initial packaging

