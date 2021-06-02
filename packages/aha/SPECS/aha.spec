Name: aha
Version: 0.5
Release: 3%{?dist}
Summary: Convert terminal output to HTML

License: MPLv1.1 or LGPLv2+
URL: https://github.com/theZiz/aha
Source0: %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc make


%description
%{name} parses output from other programs,
recognizes ANSI terminal escape sequences
and produces an HTML rendition of the original text.


%prep
%setup -q
# Extract license header from source code
cat aha.c | awk '1;/\*\//{exit}' > LICENSE


%build
%set_build_flags
%make_build


%install
%make_install PREFIX=%{_prefix}


%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Artur Iwicki <fedora@svgames.pl> - 0.5-1
- Update to latest upstream release

* Wed Jul 18 2018 Artur Iwicki <fedora@svgames.pl> - 0.4.10.6-2
- Invoke %%set_build_flags before building
- Use %%make_build instead of "make %%{?_smp_flags}"

* Sun Jul 15 2018 Artur Iwicki <fedora@svgames.pl> - 0.4.10.6-1
- Initial packaging
