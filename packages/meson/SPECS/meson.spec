# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

%global libname mesonbuild

Name:           meson
Version:        0.54.999git29ef44
Release:        2%{?dist}
Summary:        High productivity build system

License:        ASL 2.0
URL:            https://mesonbuild.com/
Source:         https://github.com/mesonbuild/meson/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Patch1000:      meson.sgifixes.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python%{python3_version}dist(setuptools)
Requires:       ninja-build

%description
Meson is a build system designed to optimize programmer
productivity. It aims to do this by providing simple, out-of-the-box
support for modern software development tools and practices, such as
unit tests, coverage reports, Valgrind, CCache and the like.

%prep
%autosetup -p1

# For patch creation
#exit 1

# Macro should not change when we are redefining bindir
sed -i -e "/^%%__meson /s| .*$| %{_bindir}/%{name}|" data/macros.%{name}

%build
%py3_build

%install
%py3_install
install -Dpm0644 -t %{buildroot}%{_rpmmacrodir} data/macros.%{name}

%files
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/%{libname}/
%{python3_sitelib}/%{name}-*.egg-info/
%{_mandir}/man1/%{name}.1*
%{_rpmmacrodir}/macros.%{name}
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy

%changelog
* Mon Jun 15 2020 Daniel Hams <daniel.hams@gmail.com> - 0.54.999git29ef44-2
- Fix up the num cpus detection logic used by some packages, enable new dependency on the compute dependency provide of setuptools

* Fri May 22 2020 Daniel Hams <daniel.hams@gmail.com> - 0.54.999git29ef44
- Upgrade to a version from GIT where maintainers have implemented code allowing to set custom rpaths via LDFLAGS rather than having to modify the projects themselves.

* Thu May 21 2020 Daniel Hams <daniel.hams@gmail.com> - 0.52.0-2
- Fix up machine/arch detection for all mips

* Wed Oct 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.52.0-1
- Update to 0.52.0

* Mon Aug 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.51.2-1
- Update to 0.51.2

* Wed Jul 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.51.1-1
- Update to 0.51.1

* Wed Apr 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.50.1-1
- Update to 0.50.1

* Mon Apr 08 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.50.0-2
- Fix -Db_ndebug=if-release with -Dbuildtype=plain

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.50.0-1
- Update to 0.50.0

* Mon Feb 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.49.2-1
- Update to 0.49.2

* Wed Jan 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.49.1-1
- Update to 0.49.1

* Sun Dec 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.49.0-1
- Update to 0.49.0

* Sat Dec 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.48.2-1
- Initial package
