Name:           libmawk
Version:        1.0.2
Release:        2%{?dist}
Summary:        Embed awk scripting language in any application written in C

License:        GPLv2
URL:            http://repo.hu/projects/libmawk
Source0:        http://repo.hu/projects/libmawk/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
Libmawk is a fork of mawk 1.3.3 restructured for embedding.
This means the user gets libmawk.h and libmawk.so and can embed
awk scripting language in any application written in C.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
HTML documentation for %{name}.


%prep
%autosetup


%build
./"configure" --prefix=%{_prefix} --libarchdir=%{_libdir} --symbols \
  --CFLAGS="%{build_cflags}" --LDFLAGS="%{build_ldflags}"
%make_build


%install
%make_install LIBARCHDIR=%{buildroot}/%{_libdir} LIBPATH=%{buildroot}/%{_libdir}/%{name}


%files
%license src/libmawk/COPYING
%doc AUTHORS README Release_notes
%{_libdir}/*.so.1*
%{_bindir}/lmawk
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.awk
%{_mandir}/man1/*

%files devel
%{_mandir}/man3/*
%{_mandir}/man7/*
%{_includedir}/*
%{_libdir}/*.so

%files doc
%doc %{_docdir}/%{name}


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Alain <alain vigne 14 AT gmail com> - 1.0.2-1
- New upstream release
- Add build flags to local "configure"
- Own libdir/name directory

* Sun Mar 17 2019 Alain <alain vigne 14 AT gmail com> - 1.0.1-2
- use proper libarchdir ./configure switch

* Thu Feb 28 2019 Alain <alain vigne 14 AT gmail com> - 1.0.1-1
- New upstream release
- Install awklib library
- Install man pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 01 2018 Alain <alain vigne 14 AT gmail com> - 1.0.0-1
- Initial proposal
