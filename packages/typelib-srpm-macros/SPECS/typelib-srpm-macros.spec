Name:           typelib-srpm-macros
Version:        1
Release:        4%{?dist}
Summary:        gobject-introspection typelib sub-package generator macros

URL:            https://src.fedoraproject.org/rpms/typelib-srpm-macros
License:        Public Domain
Source0:        macros.typelib

BuildArch:      noarch

%description
RPM macros for generating typelib sub-packages for gobject-introspection
enabled library packages

%prep
echo "These files herefore released into the Public Domain" > COPYING


%install
install -D -p %{SOURCE0} $RPM_BUILD_ROOT%{_rpmmacrodir}/macros.typelib


%files
%license COPYING
%{_rpmmacrodir}/macros.typelib


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Yanko Kaneti <yaneti@declera.com> - 1-1
- Initial spec + suggestions from review
