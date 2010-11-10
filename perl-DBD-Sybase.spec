%define upstream_name    DBD-Sybase
%define upstream_version 1.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Sybase database driver for the DBI module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/~mewp/DBD-Sybase/
Source0:	http://search.cpan.org/CPAN/authors/id/M/ME/MEWP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	freetds-devel
BuildRequires:	gettext-devel
BuildRequires:	perl-DBI >= 1.00
BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
DBD::Sybase is a Perl module which works with the DBI module to provide access
to Sybase databases. With FreeTDS DBD::Sybase can be also used to query a
MS-SQL 7 or 2000 database server from a UNIX/Linux host.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
export SYBASE=%{_prefix}
echo -e "\n\n\n\n\n\n" | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}" LD_RUN_PATH=""

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README
%{perl_vendorarch}/DBD/Sybase.pm
%{perl_vendorarch}/DBD/dbd-sybase.pod
%dir %{perl_vendorarch}/auto/DBD/Sybase
%attr(0755,root,root) %{perl_vendorarch}/auto/DBD/Sybase/Sybase.so
%{_mandir}/man3/*
