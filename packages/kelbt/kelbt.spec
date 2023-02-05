Name:           kelbt
Version:        0.16
Release:        9%{?dist}
Summary:        Backtracking LR Parsing

# aapl/ is the LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            http://freecode.com/projects/kelbt
Source0:        https://www.colm.net/files/%{name}/%{name}-%{version}.tar.gz
Patch0:         %{name}-signed-char.diff

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake

# Unfortunately, upstream doesn't exist and not possible to find version
Provides:       bundled(aapl)

%description
Kelbt generates backtracking LALR(1) parsers. Where traditional
LALR(1) parser generators require static resolution of shift/reduce
conflicts, Kelbt generates parsers that handle conflicts by
backtracking at runtime. Kelbt is able to generate a parser for any
context-free grammar that is free of hidden left recursion.

%prep
%autosetup -p1

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog
%{_bindir}/%{name}

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.16-2
- Rename patch

* Fri Oct 07 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.16-1
- Initial package
