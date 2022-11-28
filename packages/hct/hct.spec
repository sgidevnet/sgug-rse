Name:           hct
Version:        0.7.60
Release:        26%{?dist}
Summary:        A HDL complexity tool

License:        GPLv3 and LGPLv3
URL:            http://hct.sourceforge.net/
Source0:        http://downloads.sourceforge.net/hct/hct-%{version}.tar.gz
Source1:        Makefile.PL
Patch0:         hct-set-env-hcthome.patch
Patch1:         hct-set-hct-path-for-moved-lang.patch 
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%{?perl_default_filter}

%description 
The goal of the HCT is to generate scores that represent
the complexity of the constituent modules of large 
integrated circuit design projects – i.e. SOCs. The design's 
complexity scores are useful to verification
teams so as to efficiently focus resources based on the dynamic
complexity profile of a design. The scores are a useful tool to guide
HDL designer's re-factoring efforts.

%prep
%setup -q -n hct-%{version}
%patch0 -p1 -b .fix
%patch1 -p1 -b .hct

%{__sed} -e "s|PERL_VENDORLIB|'%{perl_vendorlib}'|" hct.pl > hct.ex
%{__chmod} +x hct.ex
touch -r hct.pl hct.ex
%{__mv} hct.ex hct

%{__cp} lang/hdl/vhdl/parser.pm parser.ex
dos2unix parser.ex
touch -r lang/hdl/vhdl/parser.pm parser.ex
%{__mv} parser.ex lang/hdl/vhdl/parser.pm

find . -depth \( -name 'config*'   -o  \
                 -name 'windows'   -o  \
                 -name 'Misc'      -o  \
                 -name 'Pod'       -o  \
                 -name '.svn'      -o  \
                 -name '*.svn'         \) \
  -exec %{__rm} -rf -- '{}' +

find . -depth \( -name 'Makefile*' -o   \
                 -name '*sh'       -o  \
                 -name '*.output'  -o  \
                 -name '*.yp'      -o  \
                 -name '*.y'       -o  \
                 -name '*.l'       -o  \
                 -name '*.hct'     -o  \
                 -name '.*pm'      -o  \
                 -name '\.\_*'     -o  \
                 -name '\#*'           \) \
  -exec %{__rm} -f -- '{}' +

%{__rm} -f src/perllib/HCT/Lang/YappParserTracer.pm

%{__chmod} -x src/perllib/HCT.pm
%{__chmod} -x lang/hdl/verilog.pm
%{__chmod} -x lang/README
%{__chmod} -x lang/hdl/cdl/lexer.pm
%{__chmod} -x lang/hdl/cdl.pm
%{__chmod} -x lang/hdl/vhdl/parser.pm
%{__chmod} -x lang/hdl/verilog/lexer.pm

%{__mkdir} lib
%{__mv} src/perllib/* lib/
%{__mv} lang lib/HCT
%{__rm} -rf src
%{__cp} %{SOURCE1} %{_builddir}/%{name}-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test TEST_VERBOSE=1

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{__rm} -f %{buildroot}/%{perl_vendorlib}/hct.pl

%{_fixperms} %{buildroot}/*

%files
%doc COPYING COPYING.LESSER README
%{perl_vendorlib}/*
%{_bindir}/hct
%{_mandir}/man3/*

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.60-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.60-25
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.60-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.60-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.60-22
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.60-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.60-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.60-19
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.60-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.60-17
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.60-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.60-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.60-14
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.7.60-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.60-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.60-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.7.60-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.60-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.60-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.7.60-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.60-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.7.60-5
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jun 27 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 0.7.60-3
- Rebuild for perl-5.12.
- Remove redundant R: perl-Parse-Yapp.

* Wed Jun 16 2010 Shakthi Kannan <shakthimaan [AT] gmail dot com> 0.7.60-2
- Appended slash in URL.
- Expanded IC as integrated circuits in description.
- Changed rm rf to use find syntax.
- Changed Makefile.PL to use hct instead of hct.pl.

* Thu May 13 2010 Shakthi Kannan <shakthimaan [AT] gmail dot com> 0.7.60-1
- Initial Fedora RPM version
